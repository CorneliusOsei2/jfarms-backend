"""Added employees.date_of_birth

Revision ID: 7abfbf50f555
Revises: 446a6f1d26c7
Create Date: 2023-03-08 12:40:21.565823

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7abfbf50f555'
down_revision = '446a6f1d26c7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clients_sales')
    op.drop_index('ix_clients_email', table_name='clients')
    op.drop_index('ix_clients_full_name', table_name='clients')
    op.drop_index('ix_clients_id', table_name='clients')
    op.drop_index('ix_clients_username', table_name='clients')
    op.drop_table('clients')
    op.add_column('employees', sa.Column('date_of_birth', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employees', 'date_of_birth')
    op.create_table('clients',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('clients_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('start_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('end_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='clients_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_clients_username', 'clients', ['username'], unique=False)
    op.create_index('ix_clients_id', 'clients', ['id'], unique=False)
    op.create_index('ix_clients_full_name', 'clients', ['full_name'], unique=False)
    op.create_index('ix_clients_email', 'clients', ['email'], unique=False)
    op.create_table('clients_sales',
    sa.Column('client_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sale_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], name='clients_sales_client_id_fkey'),
    sa.ForeignKeyConstraint(['sale_id'], ['sales.id'], name='clients_sales_sale_id_fkey')
    )
    # ### end Alembic commands ###
