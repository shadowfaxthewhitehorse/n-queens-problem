package main

import (
	"fmt"
	"math"
)

type position struct {
	row, col int
}
//
//
// PROBLEM STATEMENT
// 
// solve the n queens problem with the additional constraint that 
// queens can also move like knights, and so one must make sure that
// no queen can capture another queen using a knight move.


func solveNQueens(n int) [][]position {
	board := make([][]bool, n)
	for i := range board {
		board[i] = make([]bool, n)
	}
	solutions := [][]position{}
	solveNQueensHelper(board, 0, &solutions)
	return solutions
}

func solveNQueensHelper(board [][]bool, col int, solutions *[][]position) {
	// Base case: all queens have been placed
	if col == len(board) {
		positions := []position{}
		for i := 0; i < len(board); i++ {
			for j := 0; j < len(board); j++ {
				if board[i][j] {
					positions = append(positions, position{i, j})
				}
			}
		}
		*solutions = append(*solutions, positions)
		return
	}

	// Try placing a queen in each row of the current column
	for row := 0; row < len(board); row++ {
		if isSafe(board, row, col) {
			board[row][col] = true
			solveNQueensHelper(board, col+1, solutions)
			board[row][col] = false
		}
	}
}

func isSafe(board [][]bool, row int, col int) bool {
	// Check the row
	for i := 0; i < col; i++ {
		if board[row][i] {
			return false
		}
	}

	// Check the upper diagonal
	i, j := row, col
	for i >= 0 && j >= 0 {
		if board[i][j] {
			return false
		}
		i--
		j--
	}

	// Check the lower diagonal
	i, j = row, col
	for i < len(board) && j >= 0 {
		if board[i][j] {
			return false
		}
		i++
		j--
	}

	// Check for knight attacks
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board); j++ {
			if board[i][j] && (math.Abs(float64(row-i)) == 2 && math.Abs(float64(col-j)) == 1 ||
				math.Abs(float64(row-i)) == 1 && math.Abs(float64(col-j)) == 2) {
				return false
			}
		}
	}

	// All checks passed, it is safe to place a queen here
	return true
}

func printBoard(board [][]bool) {
	for i := range board {
		for j := range board[i] {
			if board[i][j] {
				fmt.Print("Q ")
			} else {
				fmt.Print(". ")
			}
		}
		fmt.Println()
	}
	fmt.Println()
}

func main() {
	// Test the program with a 4x4 board
	solutions := solveNQueens(4)
	for _, solution := range solutions {
		board := make([][]bool, 4)
		for i := range board {
			board[i] = make([]bool, 4)
		}
		for _, pos := range solution {
			board[pos.row][pos.col] = true
		}
		printBoard(board)
	}
}
