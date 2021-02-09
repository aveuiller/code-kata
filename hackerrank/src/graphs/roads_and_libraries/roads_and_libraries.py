#!/bin/python3

import os


def dfs(i, links, visited):
    """
    This one is working.
    :param i:
    :param links:
    :param visited:
    :return:
    """
    visited.add(i)
    return 1 + sum([dfs(n, links, visited)
                    for n in links.get(i, []) if n not in visited])


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    """
    # Challenge: https://www.hackerrank.com/challenges/torque-and-development

    :param n:
    :param c_lib:
    :param c_road:
    :param cities:
    :return:
    """
    if c_road > c_lib:
        return c_lib * n

    links = {}
    for c1, c2 in cities:
        c1_links = links.setdefault(c1, [])
        c1_links.append(c2)
        c2_links = links.setdefault(c2, [])
        c2_links.append(c1)

    visited = set()
    return sum([(dfs(i, links, visited) - 1) * c_road + c_lib
                for i in range(1, n + 1) if i not in visited])

    # return dfs_iterative(n, c_lib, c_road, links)


def dfs_iterative(n, c_lib, c_road, links):
    """
    This one times-out

    :param n:
    :param c_lib:
    :param c_road:
    :param links:
    :return:
    """
    stack = [1]
    available = {i for i in range(1, n + 1)}
    visited = set()
    comp_size = 0
    price = 0
    while len(visited) < n:
        current = stack.pop()
        # print(f"---------")
        # print(f"Stack: {stack}")
        # print(f"Current: {current}")
        # print(f"Comp-size: {comp_size}")
        # print(f"price: {price}")

        if current not in visited:
            comp_size += 1
            visited.add(current)
            stack += links.get(current, [])

        if not stack:
            price += c_lib + (comp_size - 1) * c_road
            comp_size = 0
            remaining = list(available - visited)
            if remaining:
                stack.append(remaining[0])

    if comp_size:
        price += c_lib + (comp_size - 1) * c_road
    return price


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])
        m = int(nmC_libC_road[1])
        c_lib = int(nmC_libC_road[2])
        c_road = int(nmC_libC_road[3])
        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()


if __name__ == '__main__':
    main()
