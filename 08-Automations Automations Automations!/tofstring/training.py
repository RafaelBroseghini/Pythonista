def main():
    bfs(GRAPH, "Kevin Bacon")
    inp = input(
        "Enter name of actor/actress (exit to stop) for their Kevin Bacon number: "
    )

    while inp != "exit":
        if inp == "Kevin Bacon":
            print("0 of course!")
        else:
            result = traverse(GRAPH, inp, "Kevin Bacon")
            print("{}'s Kevin Bacon numbers is: {}".format(inp, len(result)))
            for actor in range(len(result) - 1):
                pred = GRAPH[result[actor]].getPred()
                movie_in_common = GRAPH[result[actor]][pred]
                print(
                    "{} acted with {} in {}".format(
                        result[actor], pred, movie_in_common
                    )
                )

        inp = input(
            "Enter name of actor/actress (exit to stop) for their Kevin Bacon number:"
        )
