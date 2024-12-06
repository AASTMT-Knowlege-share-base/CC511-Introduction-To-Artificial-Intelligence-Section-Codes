def minimax(node, depth, is_maximizing_player):
    """
    Minimax Algorithm: Recursively calculates the best score.
    :param node: Current node value or game tree (list for children).
    :param depth: Current depth in the tree.
    :param is_maximizing_player: True if MAX's turn, False if MIN's turn.
    :return: Best score for the player at this node.
    """
    # Base case: If the node is a terminal node, return its value
    if isinstance(node, int):
        return node

    if is_maximizing_player:
        max_eval = float('-inf')
        for child in node:  # Explore all children
            eval = minimax(child, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in node:  # Explore all children
            eval = minimax(child, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


# Example usage
if __name__ == "__main__":
    # Example game tree
    game_tree = [
        [3, 5],        # Node B (MIN)
        [6],           # Node C (MIN)
        [0, 9]         # Node D (MIN)
    ]
    
    # MAX's turn at the root
    result = minimax(game_tree, depth=0, is_maximizing_player=True)
    print(f"The optimal value for MAX is: {result}")
