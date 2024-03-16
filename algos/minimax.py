def minimax(position): 
    if position.is_terminal(): 
        return position.utility() 
    if position.to_move() == 'X': 
        best_score = -infinity 
        for move in position.moves(): 
                score = minimax(position.result(move)) 
                best_score = max(best_score, score) 
        return best_score 
    else: 
        position.to_move() == 'O' 
        best_score = infinity 
        for move in position.moves(): 
            score = minimax(position.result(move)) 
            best_score = min(best_score, score) 
        return best_score