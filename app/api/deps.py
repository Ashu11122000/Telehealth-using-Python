# Import Depends → for dependency injection
# It allows automatic injection of required components (like DB, auth, etc.)
# HTTPException → to return proper API errors
# status → for standard HTTP status codes
from fastapi import Depends, HTTPException, status

# OAuth2PasswordBearer → extracts token from Authorization header
# It extracts JWT token from Authorization header (Bearer <token>)
from fastapi.security import OAuth2PasswordBearer

# Import DB session
# Session is used to interact with the database (query, commit, etc.)
from sqlalchemy.orm import Session

# Import Database dependency function
# get_db() provides a DB session (dependency injection)
from app.db.session import get_db

# Import JWT decoder function
# This function verifies and decodes JWT token into payload (dict)
from app.core.security import decode_access_token

# Import User model
# Represents user table in database
from app.models.user import User

# OAuth2 scheme definition (used by Swagger + token extraction)
# tokenUrl -> tells Swagger UI where login API is located
# Swagger uses this to generate "Authorize" button
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# 1. GET CURRENT USER
def get_current_user(
    
    # token is automatically extracted from Authorization header
    # Example: Authorization: Bearer <JWT_TOKEN>
    token: str = Depends(oauth2_scheme),
    
    # db session is injected automatically using get_db()
    db: Session = Depends(get_db)
):
    """
    Extract and validate JWT token,
    then return the corresponding user.
    """

    # Decode JWT token
    # This verifies signature + expiration
    # Returns payload (dictionary) if valid
    payload = decode_access_token(token)

    # Token invalid or expired -> payload will be None
    if not payload:
        raise HTTPException(
            
            # 401 -> Unauthorized
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    # Extract user ID from payload
    # sub (subject) is standard JWT field used for user identity
    user_id = payload.get("sub")

    # If user_id is missing -> token is malformed
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )

    # Query database to fetch user
    # db.query(User) -> SELECT * FROM users
    # filter(User.id == int(user_id)) -> WHERE id = user_id
    # first() -> returns first result or None
    user = db.query(User).filter(User.id == int(user_id)).first()

    # If user does not exits in DB
    if not user:
        raise HTTPException(
            # 404 -> Not Found
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
        
    # Return authenticated user object
    return user

# 2. ACTIVE USER CHECK
def get_current_active_user(
    
    # This depends on get_current_user -> chaining dependencies
    current_user: User = Depends(get_current_user)
):
    """
    Ensure user is active.
    """
    
    # Check if user is inactive
    # is_active is typically a boolean column in DB
    if not current_user.is_active:
        raise HTTPException(
            
            # 400 -> Bad Request
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
        
    # Return active user
    return current_user

# 3. ROLE-BASED ACCESS CONTROL (RBAC)
def require_role(allowed_roles: list):
    """
    Restrict access based on user role.
    
    Example:
    Depends(require_role(["admin"]))
    """
    
    # Inner function (closure)
    # This function will be executed by FastAPI dependency system
    def role_checker(
        
        # First ensure user is authenticated and active
        current_user: User = Depends(get_current_active_user)
    ):
        
        # check if user's role is in allowed roles list
        if current_user.role not in allowed_roles:
            raise HTTPException(
                # 403 -> Forbidden
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action"
            )
            
            # If role is allowed -> return user
        return current_user
    
    # Return the inner function
    # FastAPI will use this as dependency
    return role_checker