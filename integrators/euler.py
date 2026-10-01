
def forward_euler (f,df,dt):
    """ 
    :f: function value at current step
    :df: function derivatie value at current step
    :dt: timestep
    :y: function value at next step
    """
    y = f + df*dt

    return y