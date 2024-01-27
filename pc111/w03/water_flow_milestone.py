def water_column_height(tower_height, tank_height):
    """
    Calculate the total height of the water column 
    considering the tower height and tank height.
    """
    return tower_height + ((3 * tank_height) / 4)

def pressure_gain_from_water_height(height):
    """
    Calculate the pressure gain due to the height 
    of the water column.
    """
    return (998.2 * 9.80665 * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, 
friction_factor, fluid_velocity):
    """
    Calculate the pressure loss in a pipe based on 
    the pipe diameter, pipe length, friction factor, 
    and fluid velocity.
    """
    return (-friction_factor * pipe_length * 998.2 * fluid_velocity ** 2) / (2000 * pipe_diameter)
