print(sum([(((-1)**(i//2-1))*4)/(i*(i+1)*(i+2)) for i in range(2,201,2)])+3)