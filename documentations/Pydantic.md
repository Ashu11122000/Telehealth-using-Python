# Pydantic – Complete Guide

# Overview

# What is Pydantic?

Pydantic is a Python library used for data validation and parsing using type hints.

--- 

# What it does?

* Ensures that input data matches expected types (e.g., int, str, email)
* Automatically converts data into the correct type when possible
* Raises clear errors if data is invalid

---

# Why use it?
* **Data Validation** Prevents invalid or malformed data
* **Type Safety** Uses Python type hints to enforce structure
* **Automatic Parsing** Converts Data
* **Clean Code** Reduces manual validation logic
* **FastAPI integration** Core library used in FastAPI for request/response validation

---

# Key features (data validation, parsing etc.)
**Data Validation** Process of ensuring data is clean, correct, and useful before it is processed, stored, and analyzed.

**Data Parsing** Process of analyzing, breaking down and converting the raw, unstructured data into a readable, structured format (like JSON) that software can easily understand.

---

# Where it is used?

Pydantic as a smart gatekeeper.
* We give some data (from APIs, files, etc.), it checks data is correct or not?

| Situation                       | What Pydantic Does?                       | Result                  |
| ------------------------------- | ----------------------------------------- | ----------------------- |
| API sends messy data            | Cleans & converts data types              | Structured, usable data |
| User gives wrong input          | Validates input & shows errors            | Safe input handling     |
| Environment variables (strings) | Converts to correct types (`int`, `bool`) | Avoids bugs             |

---

# Installation

```bash
pip install pydantic
```

**What this actually install?**
This installs the core Pydantic package.
Internally, we get:
* Core validation engine (written in Python + Rust-backed core in newer versions)
* Type validation system (based on Python type hints)
* Error handling system

**Why only pip install pydantic is enough?**
Because: 
* It includes everything needed for validation
* No extra dependencies required for basic usage
* Work standalone (even without FastAPI)

**Optional (for dotenv / settings)**

```bash
pip install pydantic[dotenv]
```

* This is called an extra dependency group.
* It tells pip: Install Pydantic + additional packages needed for dotenv support.
* It installed additionally: python-dotenv package
* A dotenv (.env) file stores environment variables. 

**pydantic** = data validation layer
**pydantic[dotenv]** = configuration management layer

---

# Core Concepts

## BaseModel

**BaseModel** is the core class provided by Pydantic used to: Define data schemas (models) with validation and type enforcement.

* Foundation of Pydantic
* Defines data structures/data types
* Adding type rules → using standard Python type hints and the **field()** function for added **constraints**.

**field() function** use to provide metadata and validation constraints for model fields beyond their basic type annotations.

**Constraints** conditions or rules that a variable must satisfy for solution or program to be considered valid.

### Purpose of BaseModel

BaseModel is used to: 
* Validate incoming data
* Enforce data types using Python type hints
* Automatically convert data (parsing)
* Provide structured, predictable objects

### What happens internally in BaseModel?
When we create a model using BaseModel:
1. Reads type annotation (str, int, etc.)
2. Validates input data
3. Convert types if possible ("25" -> 25)
4. Raises error if invalid

### Why BaseModel is important?

Without BaseModel:
* Manual validation (if/else) everywhere
* High chances of bugs

With BaseModel:
* Clean, centralized validation
* Safer and more maintainable code

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: str

# Input data
user = User(name = "Ashish", age = "25")

print(user)
```

```output
name = 'Ashish' age = 25
```

---

## Data Validation

Data Validation ensures that incoming data:
* Has the correct type (int, str, etc.)
* Follows defined rules (e.g., age>= 0)
* Is safe and usable
* In Pydantic, this happens automatically using models.

## How Pydantic validates data automatically?

* Reads type hints

```python
age: int
```

* Receives input data
```python
age = "25"
```

* Tries to parse (convert)
"25" → 25

* Applies validation rules and checks constraints (e.g., age>=0)

* Raises error if invalid
"abc" → ValidationError

### Example of Data Validation

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int = Field(..., ge = 0)    # age must be >= 0

# Valid input
user = User(name = "Ashish", age = "25")
print(user)
```
```output
name = 'Ashish' age = 25
```

### Why this matters in real applications?
* API input → validated automatically
* User Input → errors caught early
* Prevents runtime crashes
* Keeps data clean and predictable

---

## Type Hints

* Type hints are annotations in Python that specify the expected data type of a variable.
* In simple terms, Type hints tells Python and Pydantic: "What type of data type should be here?"

```python
name: str
age: int
price: float
is_active: bool
```

* Python interpreter reads data types internally but do not print data types in output.

### Role of Python type hints in Pydantic

In Pydantic, type hints become powerful because they are used to:
* Define the structure of data
* Validate input data
* Automatically converts types (parsing)
* Generate clear error messages

**Type hints + Pydantic** = Runtime Validation System

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool

user = User(name = "Ashish", age = "25", is_active = "true")
```

---

## Field & Constraints

In Pydantic, Field is used to add extra validation rules (constraints) and metadata to model fields.

### Why use Field?

By default, type hints only checks data types:
```python
age: int
```
But Field comes when we want:
* Age >= 0
* Name length >= 3
* Price > 0

### Using Field for validations

| Constraint   | Meaning               |
| ------------ | --------------------- |
| `ge`         | Greater than or equal |
| `gt`         | Greater than          |
| `le`         | Less than or equal    |
| `lt`         | Less than             |
| `min_length` | Minimum string length |
| `max_length` | Maximum string length |
| `regex`      | Pattern matching      |

### Example of Field and Constraints

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=0, le=120)
    email: str = Field(..., regex=r"^\S+@\S+\.\S+$")

# Valid input
user = User(name="Ashish", age=25, email="ashish@gmail.com")
print(user)
```

---

## Default Values

A default value is the value a variable/field takes if the user does not give any input.

When a field has a default value:

- It becomes **optional in input**
- If user does not provide it → Pydantic automatically assigns default
- If user provides value → that value overrides default

## Internal Behavior

1. Check if field is provided  
2. If NOT → use default value  
3. Validate the default value as well  

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int = 18   # Default value
    is_active: bool = True

user = User(name="Ashish")
print(user)

```

---

## Optional Fields
Optional fields are fields that:
* May or may not be provided  
* Can explicitly have a value of `None`

### Example of Optional Fields
```python
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    phone: Optional[str] = None
    bio: str | None = None

user = User(name="Ashish")
print(user)
```

---

## Nested Models

Nested models allow you to:

* Use one Pydantic model inside another model
* This helps represent complex, structured data (just like real-world relationships).
* Real-world data is often hierarchical:
  - User → Address  
  - Order → Items  
  - Doctor → Profile  

* Instead of flat data, we use nested schemas
* Each model validates its own data independently

## How it Works Internally?

1. Outer model receives input data  
2. Detects nested model field  
3. Converts dictionary → nested model object  
4. Validates nested fields separately  
5. Combines everything into one structured object  

### Example of Nested Models

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    address: Address   # Nested model

user = User(
    name="Ashish",
    address={
        "city": "Delhi",
        "pincode": "110001"
    }
)

print(user)
```

---

## Model Parsing

Converting raw input data (dict, JSON, etc.) into a structured Pydantic model with proper types.

In real applications, data usually comes as:

* JSON (API requests)
* Dictionaries
* Strings (from forms, env variables)

This data is often:
* Unstructured 
* Incorrect types 

### Parsing = Conversion + Validation

Pydantic does two things together:

1. **Parsing (Conversion)**  
   * `"25"` → `25`  
   * `"true"` → `True`

2. **Validation**  
   * Ensures data follows defined rules  

### Internal Flow

1. Receive raw input (dict/JSON)  
2. Match keys with model fields  
3. Convert values to correct types  
4. Apply validations  
5. Return structured object OR raise error

### Example of Model Parsing

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool

data = {
    "name": "Ashish",
    "age": "25",
    "is_active": "true"
}

user = User(**data)   # Parsing happens here

print(user)
```

---

## Model Serialization

Converting a Pydantic model into standard data formats (dict, JSON, etc.)

After parsing and validation, your data is stored as a **Python object**.

But in real applications, you often need to:

* Send data as API response (JSON)
* Store in database
* Log or transfer data

|     Stage     |    Direction     |
|---------------|------------------|
|    Parsing    | Raw data → Model |
| Serialization | Model → Raw data |

### How it Works Internally?

1. Take model instance  
2. Extract field values  
3. Convert into standard format (`dict` / JSON)  
4. Handle nested models automatically

### Example of Model Serialization

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool

user = User(name="Ashish", age=25, is_active=True)

data_dict = user.model_dump()   # Convert to dict
print(data_dict)
```

## Model Configuration

Customize how a model behaves during validation, parsing, and serialization

By default, Pydantic has standard behavior:

* Accepts matching fields only  
* Allows type conversion  
* Includes all fields in output  
* But real-world applications need more control.

### What Can You Configure?

Common configurations include:

|         Setting        |           Purpose       | 
|------------------------|-------------------------|
|          `extra`       |   Handle extra fields   |
| `str_strip_whitespace` |   Remove extra spaces   |
|  `validate_assignment` |    Validate on update   |
|   `populate_by_name`   |    Allow alias usage    |
|        `frozen`        |   Make model immutable  |
|    `from_attributes`   | Read data from objects  |

### Example of Model Configuration

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    name: str
    age: int

    model_config = ConfigDict(
        extra="forbid",              # reject unknown fields
        str_strip_whitespace=True,  # remove spaces
        validate_assignment=True    # validate on update
    )

# Valid input
user = User(name="  Ashish  ", age=25)
print(user)

# Updating value (validated)
user.age = 30
```

---

# Validators

Add custom validation logic beyond basic type checks and constraints.

---

## Field Validators

Field validators are used to validate or modify individual fields.

* Applied to a single field
* Runs during model validation
* Can:
  - Clean data (e.g., strip spaces)
  - Enforce custom rules
  - Transform values

# Example

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int

    @field_validator("name")
    @classmethod
    def name_must_be_valid(cls, value):
        if len(value.strip()) < 3:
            raise ValueError("Name must be at least 3 characters long")
        return value.strip()

user = User(name="  Ashish  ", age=25)
print(user)
```

---

## Root Validators

Root validators are used to validate multiple fields together (whole model)

* Works on the entire model data
* Useful when validation depends on multiple fields

### When to use?
* Password & confirm password match
* Start date < End date
* Conditional validation

### Example

```python
from pydantic import BaseModel, model_validator

class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def check_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

user = User(password="1234", confirm_password="1234")
print(user)
```

| Feature  | Field Validator      | Root Validator         |
| -------- | -------------------- | ---------------------- |
| Scope    | Single field         | Entire model           |
| Use case | Field-specific rules | Cross-field validation |
| Input    | Field value          | Whole model            |

---

## Custom Validation Logic

Define your own rules that go beyond built-in types and constraints.

Pydantic already provides:
* Type validation (`int`, `str`)
* Field constraints (`min_length`, `ge`, etc.)

But in real-world applications, you often need:

* Business rules  
* Conditional validation  
* Complex checks  

- That’s where custom validation logic comes in.

### When to Use Custom Validation?

* Password strength validation  
* Age restrictions (e.g., ≥ 18)  
* Email domain restrictions  
* Conditional logic (if X → then Y required)  

### How it Works?

Custom validation is implemented using:

- `@field_validator` → for single field logic  
- `@model_validator` → for cross-field logic  

### Example
```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one number")
        return value

user = User(username="ashish", password="pass1234")
print(user)
```

---

# Limitations
# Limitations of Pydantic

Even though Pydantic is powerful, it has some limitations you should understand in real-world applications.

---

## 1. Runtime Validation (Not Compile-Time)

### Issue
- Validation happens at runtime, not before execution

### Impact
- Errors are caught only when code runs
- Not as strict as statically typed languages

---

## 2. Performance Overhead

### Issue
- Validation + parsing adds CPU cost

### Impact
- Slower than raw Python objects
- Can affect high-performance systems

---

## 3. Complex Models Become Hard to Manage

### Issue
- Deep nesting and many validators increase complexity

### Impact
- Hard to debug  
- Reduced readability  

---

## 4. Learning Curve

### Issue
- Concepts like:
  - Validators
  - Config
  - Nested models

### Impact
- Beginners may find it confusing initially

---

## 5. Silent Type Coercion

### Issue
- Automatically converts types

```python
age = "25"  # converted to 25


# Pydantic – Complete Guide

# Overview

# What is Pydantic?

Pydantic is a Python library used for data validation and parsing using type hints.

--- 

# What it does?

* Ensures that input data matches expected types (e.g., int, str, email)
* Automatically converts data into the correct type when possible
* Raises clear errors if data is invalid

---

# Why use it?
* **Data Validation** Prevents invalid or malformed data
* **Type Safety** Uses Python type hints to enforce structure
* **Automatic Parsing** Converts Data
* **Clean Code** Reduces manual validation logic
* **FastAPI integration** Core library used in FastAPI for request/response validation

---

# Key features (data validation, parsing etc.)
**Data Validation** Process of ensuring data is clean, correct, and useful before it is processed, stored, and analyzed.

**Data Parsing** Process of analyzing, breaking down and converting the raw, unstructured data into a readable, structured format (like JSON) that software can easily understand.

---

# Where it is used (FastAPI, backend systems, APIs, etc.)

Pydantic as a smart gatekeeper.
* We give some data (from APIs, files, etc.), it checks data is correct or not?

| Situation                       | What Pydantic Does?                       | Result                  |
| ------------------------------- | ----------------------------------------- | ----------------------- |
| API sends messy data            | Cleans & converts data types              | Structured, usable data |
| User gives wrong input          | Validates input & shows errors            | Safe input handling     |
| Environment variables (strings) | Converts to correct types (`int`, `bool`) | Avoids bugs             |

---

# Installation

```bash
pip install pydantic
```

**What this actually install?**
This installs the core Pydantic package.
Internally, we get:
* Core validation engine (written in Python + Rust-backed core in newer versions)
* Type validation system (based on Python type hints)
* Error handling system

**Why only pip install pydantic is enough?**
Because: 
* It includes everything needed for validation
* No extra dependencies required for basic usage
* Work standalone (even without FastAPI)

**Optional (for dotenv / settings)**

```bash
pip install pydantic[dotenv]
```

* This is called an extra dependency group.
* It tells pip: Install Pydantic + additional packages needed for dotenv support.
* It installed additionally: python-dotenv package
* A dotenv (.env) file stores environment variables. 

**pydantic** = data validation layer
**pydantic[dotenv]** = configuration management layer

---

# Core Concepts

## BaseModel

**BaseModel** is the core class provided by Pydantic used to: Define data schemas (models) with validation and type enforcement.

* Foundation of Pydantic
* Defines data structures/data types
* Adding type rules → using standard Python type hints and the **field()** function for added **constraints**.

**field() function** use to provide metadata and validation constraints for model fields beyond their basic type annotations.

**Constraints** conditions or rules that a variable must satisfy for solution or program to be considered valid.

### Purpose of BaseModel

BaseModel is used to: 
* Validate incoming data
* Enforce data types using Python type hints
* Automatically convert data (parsing)
* Provide structured, predictable objects

### What happens internally in BaseModel?
When we create a model using BaseModel:
1. Reads type annotation (str, int, etc.)
2. Validates input data
3. Convert types if possible ("25" -> 25)
4. Raises error if invalid

### Why BaseModel is important?

Without BaseModel:
* Manual validation (if/else) everywhere
* High chances of bugs

With BaseModel:
* Clean, centralized validation
* Safer and more maintainable code

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: str

# Input data
user = User(name = "Ashish", age = "25")

print(user)
```

```output
name = 'Ashish' age = 25
```

---

## Data Validation

Data Validation ensures that incoming data:
* Has the correct type (int, str, etc.)
* Follows defined rules (e.g., age>= 0)
* Is safe and usable
* In Pydantic, this happens automatically using models.

## How Pydantic validates data automatically?

* Reads type hints

```python
age: int
```

* Receives input data
```python
age = "25"
```

* Tries to parse (convert)
"25" → 25

* Applies validation rules and checks constraints (e.g., age>=0)

* Raises error if invalid
"abc" → ValidationError

### Example of Data Validation

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int = Field(..., ge = 0)    # age must be >= 0

# Valid input
user = User(name = "Ashish", age = "25")
print(user)
```
```output
name = 'Ashish' age = 25
```

### Why this matters in real applications?
* API input → validated automatically
* User Input → errors caught early
* Prevents runtime crashes
* Keeps data clean and predictable

---

## Type Hints

* Type hints are annotations in Python that specify the expected data type of a variable.
* In simple terms, Type hints tells Python and Pydantic: "What type of data type should be here?"

```python
name: str
age: int
price: float
is_active: bool
```

* Python interpreter reads data types internally but do not print data types in output.

### Role of Python type hints in Pydantic

In Pydantic, type hints become powerful because they are used to:
* Define the structure of data
* Validate input data
* Automatically converts types (parsing)
* Generate clear error messages

**Type hints + Pydantic** = Runtime Validation System

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool

user = User(name = "Ashish", age = "25", is_active = "true")
```

---

## Field & Constraints

In Pydantic, Field is used to add extra validation rules (constraints) and metadata to model fields.

### Why use Field?

By default, type hints only checks data types:
```python
age: int
```
But Field comes when we want:
* Age >= 0
* Name length >= 3
* Price > 0

### Using Field for validations

| Constraint   | Meaning               |
| ------------ | --------------------- |
| `ge`         | Greater than or equal |
| `gt`         | Greater than          |
| `le`         | Less than or equal    |
| `lt`         | Less than             |
| `min_length` | Minimum string length |
| `max_length` | Maximum string length |
| `regex`      | Pattern matching      |

### Example of Field and Constraints

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=0, le=120)
    email: str = Field(..., regex=r"^\S+@\S+\.\S+$")

# Valid input
user = User(name="Ashish", age=25, email="ashish@gmail.com")
print(user)
```

---

## Default Values

A default value is the value a variable/field takes if the user does not give any input.

When a field has a default value:

- It becomes **optional in input**
- If user does not provide it → Pydantic automatically assigns default
- If user provides value → that value overrides default

## Internal Behavior

1. Check if field is provided  
2. If NOT → use default value  
3. Validate the default value as well  

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int = 18   # Default value
    is_active: bool = True

user = User(name="Ashish")
print(user)

```

---

## Optional Fields
Optional fields are fields that:
* May or may not be provided  
* Can explicitly have a value of `None`

### Example of Optional Fields
```python
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    phone: Optional[str] = None
    bio: str | None = None

user = User(name="Ashish")
print(user)
```

---

## Nested Models

Nested models allow you to:

* Use one Pydantic model inside another model
* This helps represent complex, structured data (just like real-world relationships).
* Real-world data is often hierarchical:
  - User → Address  
  - Order → Items  
  - Doctor → Profile  

* Instead of flat data, we use nested schemas
* Each model validates its own data independently

## How it Works Internally?

1. Outer model receives input data  
2. Detects nested model field  
3. Converts dictionary → nested model object  
4. Validates nested fields separately  
5. Combines everything into one structured object  

### Example of Nested Models

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    address: Address   # Nested model

user = User(
    name="Ashish",
    address={
        "city": "Delhi",
        "pincode": "110001"
    }
)

print(user)
```

---

## Model Parsing

Converting raw input data (dict, JSON, etc.) into a structured Pydantic model with proper types.

In real applications, data usually comes as:

* JSON (API requests)
* Dictionaries
* Strings (from forms, env variables)

This data is often:
* Unstructured 
* Incorrect types 

### Parsing = Conversion + Validation

Pydantic does two things together:

1. **Parsing (Conversion)**  
   * `"25"` → `25`  
   * `"true"` → `True`

2. **Validation**  
   * Ensures data follows defined rules  

### Internal Flow

1. Receive raw input (dict/JSON)  
2. Match keys with model fields  
3. Convert values to correct types  
4. Apply validations  
5. Return structured object OR raise error

### Example of Model Parsing

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool

data = {
    "name": "Ashish",
    "age": "25",
    "is_active": "true"
}

user = User(**data)   # Parsing happens here

print(user)
```

---

## Model Serialization

Converting a Pydantic model into standard data formats (dict, JSON, etc.)

After parsing and validation, your data is stored as a **Python object**.

But in real applications, you often need to:

* Send data as API response (JSON)
* Store in database
* Log or transfer data

|     Stage     |    Direction     |
|---------------|------------------|
|    Parsing    | Raw data → Model |
| Serialization | Model → Raw data |

### How it Works Internally?

1. Take model instance  
2. Extract field values  
3. Convert into standard format (`dict` / JSON)  
4. Handle nested models automatically

### Example of Model Serialization

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool

user = User(name="Ashish", age=25, is_active=True)

data_dict = user.model_dump()   # Convert to dict
print(data_dict)
```

## Model Configuration

Customize how a model behaves during validation, parsing, and serialization

By default, Pydantic has standard behavior:

* Accepts matching fields only  
* Allows type conversion  
* Includes all fields in output  
* But real-world applications need more control.

### What Can You Configure?

Common configurations include:

|         Setting        |           Purpose       | 
|------------------------|-------------------------|
|          `extra`       |   Handle extra fields   |
| `str_strip_whitespace` |   Remove extra spaces   |
|  `validate_assignment` |    Validate on update   |
|   `populate_by_name`   |    Allow alias usage    |
|        `frozen`        |   Make model immutable  |
|    `from_attributes`   | Read data from objects  |

### Example of Model Configuration

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    name: str
    age: int

    model_config = ConfigDict(
        extra="forbid",              # reject unknown fields
        str_strip_whitespace=True,  # remove spaces
        validate_assignment=True    # validate on update
    )

# Valid input
user = User(name="  Ashish  ", age=25)
print(user)

# Updating value (validated)
user.age = 30
```

---

# Validators

Add custom validation logic beyond basic type checks and constraints.

---

## Field Validators

Field validators are used to validate or modify individual fields.

* Applied to a single field
* Runs during model validation
* Can:
  - Clean data (e.g., strip spaces)
  - Enforce custom rules
  - Transform values

# Example

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int

    @field_validator("name")
    @classmethod
    def name_must_be_valid(cls, value):
        if len(value.strip()) < 3:
            raise ValueError("Name must be at least 3 characters long")
        return value.strip()

user = User(name="  Ashish  ", age=25)
print(user)
```

---

## Root Validators

Root validators are used to validate multiple fields together (whole model)

* Works on the entire model data
* Useful when validation depends on multiple fields

### When to use?
* Password & confirm password match
* Start date < End date
* Conditional validation

### Example

```python
from pydantic import BaseModel, model_validator

class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def check_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

user = User(password="1234", confirm_password="1234")
print(user)
```

| Feature  | Field Validator      | Root Validator         |
| -------- | -------------------- | ---------------------- |
| Scope    | Single field         | Entire model           |
| Use case | Field-specific rules | Cross-field validation |
| Input    | Field value          | Whole model            |

---

## Custom Validation Logic

Define your own rules that go beyond built-in types and constraints.

Pydantic already provides:
* Type validation (`int`, `str`)
* Field constraints (`min_length`, `ge`, etc.)

But in real-world applications, you often need:

* Business rules  
* Conditional validation  
* Complex checks  

- That’s where custom validation logic comes in.

### When to Use Custom Validation?

* Password strength validation  
* Age restrictions (e.g., ≥ 18)  
* Email domain restrictions  
* Conditional logic (if X → then Y required)  

### How it Works?

Custom validation is implemented using:

- `@field_validator` → for single field logic  
- `@model_validator` → for cross-field logic  

### Example
```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one number")
        return value

user = User(username="ashish", password="pass1234")
print(user)
```

---

# Limitations
# Limitations of Pydantic

Even though Pydantic is powerful, it has some limitations you should understand in real-world applications.

---

## 1. Runtime Validation (Not Compile-Time)

### Issue
- Validation happens at runtime, not before execution

### Impact
- Errors are caught only when code runs
- Not as strict as statically typed languages

---

## 2. Performance Overhead

### Issue
- Validation + parsing adds CPU cost

### Impact
- Slower than raw Python objects
- Can affect high-performance systems

---

## 3. Complex Models Become Hard to Manage

### Issue
- Deep nesting and many validators increase complexity

### Impact
- Hard to debug  
- Reduced readability  

---

## 4. Learning Curve

### Issue
- Concepts like:
  - Validators
  - Config
  - Nested models

### Impact
- Beginners may find it confusing initially

---

## 5. Silent Type Coercion

### Issue
- Automatically converts types

```python
age = "25"  # converted to 25

