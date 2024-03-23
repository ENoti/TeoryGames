import numpy as np
from texttable import Texttable

class Matrix:

    def __init__(self, 
                 n:int,
                 m:int, 
                 bi_matrix:bool, 
                 list: list, 
                 first_player: str, 
                 second_player: str,
                 first_player_strategies: list,
                 second_player_strategies: list):
        self.n = n
        self.m = m
        self.first_player = first_player
        self.bi_matrix = bi_matrix
        self.second_player = second_player
        self.first_player_strategies = first_player_strategies
        self.second_player_strategies = second_player_strategies
        self.matrix =  np.array(list)
    
    @staticmethod
    def input_from_console():
        
        print("Set matrix size:")
        n = int(input("Number of rows: "))
        m = int(input("Number of columns: "))
        first_player = input("Name of first player: ")
        second_player = input("Name of second player: ")
        first_player_strategies = input("Write strategies for first player: ").split(" ")
        second_player_strategies = input("Write strategies for second player: ").split(" ")
        bi_matrix = True if input("Is matrix type bi? [yes/no]") == "yes" else False

        matrix = []
        print("Write values:")
        if(bi_matrix):
            for i in range(n):
                matrix.append([])
                for j in range(m):
                    matrix[i].append(tuple(int(x) for x in input().split(",")))
        else:
            for i in range(n):
                matrix.append([])
                for j in range(m):
                    matrix[i].append(int(input()))
        return Matrix(n,m,bi_matrix,matrix,first_player,
                      second_player,first_player_strategies,second_player_strategies)
    
    @staticmethod
    def input_from_file(path: str):
        with open(path,"r") as f:
            line = f.readline()
            n, m = [int(x) for x in line.split(" ")]
            print(f"Size of matrix {n}x{m}")
            first_player, second_player = f.readline().split(" ")
            print(f"First player: {first_player}; Second player: {second_player}")
            first_player_strategies = f.readline().split(" ")
            print(f"First player stategies: {first_player_strategies}")
            second_player_strategies = f.readline().split(" ")
            print(f"Second player stategies: {second_player_strategies}")
            bi_matrix = True if f.readline().replace("\n","")=="yes" else False
            print(f"Bi type of matrix: {bi_matrix}")
            matrix = []
            if(bi_matrix):
                for i in range(n):
                    line = f.readline().split(" ")
                    matrix.append([])
                    for j in range(m):
                        matrix[i].append(tuple(int(x) for x in line[j].split(",")))
            else:
                for i in range(n):
                    line = f.readline().split(" ")
                    matrix.append([])
                    for j in range(m):
                        matrix[i].append(int(line[j]))
        return Matrix(n,m,bi_matrix,matrix,first_player,second_player,first_player_strategies,second_player_strategies)
    
    def __gettexttable__(self) -> str:
        texttable = Texttable()
        texttable.set_cols_align(["c" for _ in range(self.m+1)])
        texttable.set_cols_valign(["m" for _ in range(self.m+1)])
        texttable.add_row([" "]+[strategy for strategy in self.second_player_strategies])
        for i in range(self.n):
            texttable.add_row([self.first_player_strategies[i]] + self.matrix[i].tolist())
        res_string = f"First player: {self.first_player}. Second Player: {self.second_player}"
        return res_string+texttable.draw()

    def __str__(self) -> str:
        return self.__gettexttable__()

    def output_to_file(self,name: str):
        with open(name,"w") as f:
            f.write(self.__gettexttable__())

    
