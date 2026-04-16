# Importing required SQLAlchemy components
# Column -> Used to define a column in a database table
# Integer -> Data type for integer values
# Foreignkey -> Used to create a relationship between two tables (linking columns)
# DateTime -> Date type to store date and time
# String -> Data type to store text (varchar)
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String

# relationship -> Used to define ORM-level relationships between tables (helps access related objects easily)
from sqlalchemy.orm import relationship

# Base -> The base class for all database models (created using declarative_base())
# It tells SQLAlchemy yhat this class represents a table
from app.db.base import Base

# defining a model (table) named Appointment
class Appointment(Base):
    
    # __tablename__ -> Name of the table in the database
    # "appointments" -> This table will be created in DB with this name  
    __table__name = "appointments"
    
    # id -> Unique identifier for ech appointment
    # Integer -> Data Type
    # Primary_key = True -> Makes this column the primary key (unique + not null)
    # index = True -> Creates an index for faster search queries
    id = Column(Integer, primary_key = True, index = True)
    
    # patient_id -> Stores ID of the patient
    # ForeignKey("users.id") -> Links this column to the "id" column of "users"
    # This creates a relationship between appointments and users
    patient_id = Column(Integer, ForeignKey("users.id"))
    
    # doctor_id -> Stores ID of the doctor
    # Also linked to users.id(assuming doctors are also stored in users table)
    doctor_id = Column(Integer, ForeignKey("users.id"))
    
    # date_time -> Stores appointment date and time
    # DateTime -> Data type for date + time
    # nullable = False -> This field is required (cannot be NULL)
    date_time = Column(DateTime, nullable = False)
    
    # status -> Stores current state of appointment (e.g., booked, completed, cancelled)
    # String -> Text field
    # default = "booked" -> Default value when no value is provided
    status = Column(String, default = "booked")
    
    # relationship -> Creates ORM relationship with User model
    # "User" -> Target model name (string because class may not be defined yet)
    # foreign_keys = [patient_id] -> Specifies which column is used for this relationship
    # Allows accessing patient data like: appointment.patient
    patient = relationship("User", foreign_keys = [patient_id])
    
    # Similar to patient relationship
    # Allows accessing doctor data like: appointment.doctor
    doctor = relationship("User", foreign_keys = [doctor_id])