from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .utils import build_board, solve_puzzle

# Create your views here.

def index(request):
    necessary_args = [
        'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
        'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
        'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
        'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
        'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9',
        'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
        'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9',
        'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9',
        'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9',
    ]
    valid = False
    if request.method == "GET":
        data=request.GET.dict()
        if list(data.keys()) == necessary_args:
            valid = True
            puzzle = build_board(**data)
            solved_puzzle = solve_puzzle(puzzle)
            response_data = {
                'puzzle': puzzle,
                'solved_puzzle': solved_puzzle
            }    
    if valid:
        return JsonResponse(response_data)
    else:
        return HttpResponse('<h1>Przypal</h1>')

