"""Add models for exam management

Revision ID: 5e98e45dbd08
Revises: 91cdf4665fbc
Create Date: 2018-05-23 09:56:13.870616

"""

# revision identifiers, used by Alembic.
revision = '5e98e45dbd08'
down_revision = '91cdf4665fbc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exam_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=45), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], [u'users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_exam_status_created_by'), 'exam_status', ['created_by'], unique=False)
    op.create_table('exam_trainings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=45), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], [u'users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_exam_trainings_created_by'), 'exam_trainings', ['created_by'], unique=False)
    op.create_table('question_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('display_title', sa.String(length=45), nullable=True),
    sa.Column('widget_type', sa.String(length=64), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], [u'users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_types_created_by'), 'question_types', ['created_by'], unique=False)
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=255), nullable=False),
    sa.Column('allocated_marks', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('question_type_id', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], [u'users.id'], ),
    sa.ForeignKeyConstraint(['question_type_id'], [u'question_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_questions_created_by'), 'questions', ['created_by'], unique=False)
    op.create_index(op.f('ix_questions_question_type_id'), 'questions', ['question_type_id'], unique=False)
    op.create_table('exam_questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('allocated_marks', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], [u'users.id'], ),
    sa.ForeignKeyConstraint(['exam_id'], [u'exam_trainings.id'], ),
    sa.ForeignKeyConstraint(['question_id'], [u'questions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_exam_questions_created_by'), 'exam_questions', ['created_by'], unique=False)
    op.create_index(op.f('ix_exam_questions_exam_id'), 'exam_questions', ['exam_id'], unique=False)
    op.create_index(op.f('ix_exam_questions_question_id'), 'exam_questions', ['question_id'], unique=False)
    op.create_table('question_choices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('question_choice', sa.String(length=64), nullable=True),
    sa.Column('is_answer', sa.Boolean(), nullable=True),
    sa.Column('allocated_marks', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], [u'users.id'], ),
    sa.ForeignKeyConstraint(['question_id'], [u'questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_choices_created_by'), 'question_choices', ['created_by'], unique=False)
    op.create_table('question_topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('session_topic_id', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], [u'users.id'], ),
    sa.ForeignKeyConstraint(['question_id'], [u'questions.id'], ),
    sa.ForeignKeyConstraint(['session_topic_id'], [u'session_topic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_topics_created_by'), 'question_topics', ['created_by'], unique=False)
    op.create_index(op.f('ix_question_topics_question_id'), 'question_topics', ['question_id'], unique=False)
    op.create_index(op.f('ix_question_topics_session_topic_id'), 'question_topics', ['session_topic_id'], unique=False)
    op.create_table('training_exams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('training_id', sa.String(length=64), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=True),
    sa.Column('date_administered', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], [u'users.id'], ),
    sa.ForeignKeyConstraint(['exam_id'], [u'exam_trainings.id'], ),
    sa.ForeignKeyConstraint(['training_id'], [u'training.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_training_exams_created_by'), 'training_exams', ['created_by'], unique=False)
    op.create_index(op.f('ix_training_exams_exam_id'), 'training_exams', ['exam_id'], unique=False)
    op.create_index(op.f('ix_training_exams_training_id'), 'training_exams', ['training_id'], unique=False)
    op.create_table('exam_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('training_exam_id', sa.Integer(), nullable=True),
    sa.Column('trainee_id', sa.String(length=64), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('question_score', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], [u'users.id'], ),
    sa.ForeignKeyConstraint(['question_id'], [u'questions.id'], ),
    sa.ForeignKeyConstraint(['trainee_id'], [u'registrations.id'], ),
    sa.ForeignKeyConstraint(['training_exam_id'], [u'training_exams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_exam_results_created_by'), 'exam_results', ['created_by'], unique=False)
    op.create_index(op.f('ix_exam_results_question_id'), 'exam_results', ['question_id'], unique=False)
    op.create_index(op.f('ix_exam_results_trainee_id'), 'exam_results', ['trainee_id'], unique=False)
    op.create_index(op.f('ix_exam_results_training_exam_id'), 'exam_results', ['training_exam_id'], unique=False)
    op.add_column(u'registrations', sa.Column('assets_tracker_data', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column(u'registrations',
                  sa.Column('posted_to_assets_tracker', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.create_index('ix_registrations_posted_to_assets_tracker', 'registrations', ['posted_to_assets_tracker'],
                    unique=False)
    op.add_column(u'recruitments',
                  sa.Column('posted_to_assets_tracker', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.create_index('ix_recruitments_posted_to_assets_tracker', 'recruitments', ['posted_to_assets_tracker'],
                    unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_exam_results_training_exam_id'), table_name='exam_results')
    op.drop_index(op.f('ix_exam_results_trainee_id'), table_name='exam_results')
    op.drop_index(op.f('ix_exam_results_question_id'), table_name='exam_results')
    op.drop_index(op.f('ix_exam_results_created_by'), table_name='exam_results')
    op.drop_table('exam_results')
    op.drop_index(op.f('ix_training_exams_training_id'), table_name='training_exams')
    op.drop_index(op.f('ix_training_exams_exam_id'), table_name='training_exams')
    op.drop_index(op.f('ix_training_exams_created_by'), table_name='training_exams')
    op.drop_table('training_exams')
    op.drop_index(op.f('ix_question_topics_session_topic_id'), table_name='question_topics')
    op.drop_index(op.f('ix_question_topics_question_id'), table_name='question_topics')
    op.drop_index(op.f('ix_question_topics_created_by'), table_name='question_topics')
    op.drop_table('question_topics')
    op.drop_index(op.f('ix_question_choices_created_by'), table_name='question_choices')
    op.drop_table('question_choices')
    op.drop_index(op.f('ix_exam_questions_question_id'), table_name='exam_questions')
    op.drop_index(op.f('ix_exam_questions_exam_id'), table_name='exam_questions')
    op.drop_index(op.f('ix_exam_questions_created_by'), table_name='exam_questions')
    op.drop_table('exam_questions')
    op.drop_index(op.f('ix_questions_question_type_id'), table_name='questions')
    op.drop_index(op.f('ix_questions_created_by'), table_name='questions')
    op.drop_table('questions')
    op.drop_index(op.f('ix_question_types_created_by'), table_name='question_types')
    op.drop_table('question_types')
    op.drop_index(op.f('ix_exam_trainings_created_by'), table_name='exam_trainings')
    op.drop_table('exam_trainings')
    op.drop_index(op.f('ix_exam_status_created_by'), table_name='exam_status')
    op.drop_table('exam_status')

    op.drop_index('ix_recruitments_posted_to_assets_tracker', table_name='recruitments')
    op.drop_column(u'recruitments', 'posted_to_assets_tracker')
    op.drop_index('ix_registrations_posted_to_assets_tracker', table_name='registrations')
    op.drop_column(u'registrations', 'posted_to_assets_tracker')
    op.drop_column(u'registrations', 'assets_tracker_data')
    # ### end Alembic commands ###
