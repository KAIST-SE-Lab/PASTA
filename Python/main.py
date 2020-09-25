from adaptation_planner_layer.ManagingSystem import ManagingSystem

if __name__ == '__main__':
    managingSys = ManagingSystem()

    i = 0
    while i < 10:
        managingSys.adaptManagedSystem()
        i += 1
