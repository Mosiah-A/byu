from water_flow_milestone import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
from pytest import approx
import pytest

def test_water_column_height():
    """Test the water column height function by calling it and
    comparing the values it returns to the expected values.
    """
    assert water_column_height(0.0 , 0.0) == approx(0.0)
    assert water_column_height(0.0 , 10.0) == approx(7.5)
    assert water_column_height(25.0 , 0.0) == approx(25.0)
    assert water_column_height(48.3 , 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    """Test the pressure gain from water height function by calling it and
    comparing the values it returns to the expected values.
    """
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    """Test the pressure loss from pipe function by calling it and
    comparing the values it returns to the expected values.
    """
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])