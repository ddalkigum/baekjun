bridge_length = 100
weight = 100
truck_weights = [10]


def solution(bridge_length, weight, truck_weights):
    from collections import deque
    on_bridge=[]
    pass_truck = []
    deq = deque(truck_weights)
    time = 0
    count = 0
    while truck_weights:
        try:
            truck = deq.popleft()
            if sum(on_bridge) + truck <= 10:
                on_bridge.append(truck)
            else:
                deq.appendleft(truck)
            if count == bridge_length:
                on_truck = on_bridge.pop(0)
                pass_truck.append(on_truck)
                count = 0
            count += 1
            time += 1
        except IndexError:
            print(time)
            return time
    return time

solution(bridge_length, weight, truck_weights)