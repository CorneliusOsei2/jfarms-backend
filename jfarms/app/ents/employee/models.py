import uuid

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Table,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.base_class import Base


class EmployeeID(Base):
    __tablename__ = "employee_ids"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    employee_id = Column(
        UUID(as_uuid=True),
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=True,
    )
    initials = Column(String, nullable=False)
    tag = Column(String, nullable=False)


class Sale(Base):
    __tablename__ = "sales"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    balance = Column(Float, default=0.0)


employees_sales = Table(
    "employees_sales",
    Base.metadata,
    Column("employee_id", ForeignKey("employees.id", ondelete="CASCADE")),
    Column("sale_id", ForeignKey("sales.id", ondelete="CASCADE")),
)


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, default=uuid.uuid4, index=True)
    public_id = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True)
    image = Column(String, nullable=True)
    first_name = Column(String, index=True, nullable=False)
    middle_name = Column(String, index=True, nullable=True)
    last_name = Column(String, index=True, nullable=False)
    full_name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    contact = Column(String, unique=False, nullable=False)
    home_address = Column(String, nullable=False)
    password = Column(String, nullable=False)
    date_of_birth = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    job_title = Column(String, nullable=False)
    department = Column(String, nullable=False)
    work_address = Column(String, nullable=False)
    supervisor_id = Column(
        UUID(as_uuid=True), ForeignKey("employees.id"), nullable=True
    )
    monthly_salary = Column(Integer, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    sales = relationship(
        "Sale", secondary=employees_sales, cascade="delete, save-update, merge"
    )

    def __init__(
        self,
        image,
        first_name,
        middle_name,
        last_name,
        full_name,
        email,
        contact,
        home_address,
        work_address,
        monthly_salary,
        password,
        date_of_birth,
        job_title,
        department,
        supervisor_id,
        start_date,
        end_date,
        is_active,
    ) -> None:
        self.image = image
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.full_name = full_name
        self.email = email
        self.contact = contact
        self.home_address = home_address
        self.password = password
        self.date_of_birth = date_of_birth
        self.is_active = is_active
        self.job_title = job_title
        self.department = department
        self.supervisor_id = supervisor_id
        self.work_address = work_address
        self.monthly_salary = monthly_salary
        self.start_date = start_date
        self.end_date = end_date
