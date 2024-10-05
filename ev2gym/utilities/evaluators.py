def evaluate_model(model,num_episodes):
    # Esto es redundante, pero solo funciona si es un enviroment vectorizado
    env = model.get_env()
    obs = env.reset()

    stats = []
    ep_counter=0
    while True:
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)

        if done:
            stats.append(info)
            obs = env.reset()
            ep_counter+=1
            if ep_counter>=num_episodes:
                break

    # print average stats
    print("=====================================================")
    print("total_ev_served: ", sum(
        [i[0]['total_ev_served'] for i in stats])/len(stats))
    print("total_profits: ", sum(
        [i[0]['total_profits'] for i in stats])/len(stats))
    print("real_profits (no flexibility): ", sum(
        [i[0]['real_profits'] for i in stats])/len(stats))
    print("Up_flexibility (kWh): ", sum(
        [i[0]['up_capacity'] for i in stats])/len(stats))
    print("Down_flexibility (kWh): ", sum(
        [i[0]['down_capacity'] for i in stats])/len(stats))
    print("total_energy_charged: ", sum(
        [i[0]['total_energy_charged'] for i in stats])/len(stats))
    print("average_user_satisfaction: ", sum(
        [i[0]['average_user_satisfaction'] for i in stats])/len(stats))
    print("energy_user_satisfaction: ", sum(
        [i[0]['energy_user_satisfaction'] for i in stats])/len(stats))
    print("reward: ", sum([i[0]['episode']['r'] for i in stats])/len(stats))
