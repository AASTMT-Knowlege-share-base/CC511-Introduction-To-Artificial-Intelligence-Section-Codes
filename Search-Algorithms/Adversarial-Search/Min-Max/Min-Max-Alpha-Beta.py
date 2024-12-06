def alpha_beta_pruning(node, depth, alpha, beta, is_maximizing_player):
    """
    Minimax Algorithm with Alpha-Beta Pruning.
    :param node: Current node value or game tree (list for children).
    :param depth: Current depth in the tree.
    :param alpha: Best score MAX can guarantee so far.
    :param beta: Best score MIN can guarantee so far.
    :param is_maximizing_player: True if MAX's turn, False if MIN's turn.
    :return: Best score for the player at this node.
    """
    # Base case: If the node is a terminal node, return its value
    if isinstance(node, int):
        return node

    if is_maximizing_player:
        max_eval = float('-inf')
        for child in node:  # Explore all children
            #print(f"Alpha => {alpha}, beta => {beta}")
            eval = alpha_beta_pruning(child, depth + 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)  # Update alpha
            if beta <= alpha:
                print(f"Pruning at depth {depth}, alpha: {alpha}, beta: {beta}")
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for child in node:  # Explore all children
            eval = alpha_beta_pruning(child, depth + 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)  # Update beta
            if beta <= alpha:
                print(f"Pruning at depth {depth}, alpha: {alpha}, beta: {beta}, Value of node = {node}")
                break  # Alpha cutoff
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
    result = alpha_beta_pruning(game_tree, depth=0, alpha=float('-inf'), beta=float('inf'), is_maximizing_player=True)
    print(f"The optimal value for MAX is: {result}")
