from fastapi.testclient import TestClient
from ..controllers import data_analysis as controller
from ..main import app
import pytest
from ..models import data_analysis as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_data_analysis(db_session):
    # Create a sample order
    data_analysis_data = {
        "id": "1",
        "order_id": "Test",
        "date": "4/30/24",
        "item_id": "123",
        "profit_margin": "100",
        "quantity": "1"
    }

    data_analysis_object = model.DataAnalysis(**data_analysis_data)

    # Call the create function
    created_data_analysis = controller.create(db_session, data_analysis_object)

    # Assertions
    assert created_data_analysis is not None
    assert created_data_analysis.id == "1"
    assert created_data_analysis.order_id == "Test"
    assert created_data_analysis.date == "4/30/24"
    assert created_data_analysis.item_id == "123"
    assert created_data_analysis.profit_margin == "100"
    assert created_data_analysis.quantity == "1"
