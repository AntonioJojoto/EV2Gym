# EVsSimulator
A V2X Simulation Environment for large scale EV charging optimization

# TODO short term

- [ ] Do not implement the Grid model yet.
- [ ] Implement the G2V/V2G EVs gym environment.


# Future Ideas
Here, I will write down abstract ideas about the V2X problem I am trying to solve:
- Use PandaPower to simulate the grid (use it with the power transformer class id characteristics, use the storage class to simulate the chargers fro each node **aggregate many chargers to one storage** per bus)
- Support any kind of  MV or LV network for the PandaPower grid

# Limitations
- Real **time-series** grid data are required for the PandaPower grid simulator to work, for the following parts:
    1. Power transformer
    2. Loads
    3. Generators
    4. Renewable energy sources


# Assumptions
Assumptions regarding the EVsSimulator environment:
- Power that is charged and discharged is tranferred in the:
    1. charger level 
    2. parking lot/ building level
    3. transformer level
    4. grid level (PandaPower)
 
