def metodoGauss(n, A, b):    
        for k in range (0, n-1):        
            for i in range (k+1, n):            
                m = -A[i][k]/A[k][k]
                A[i][k] = 0
                for j in range (k+1, n):
                    A[i][j] = A[i][j] + m*A[k][j]
                b[i] = b[i] + m*b[k]        
        print "Matriz A"
        for i in range(n):
            print A[i] 
        print "b = ", b
		
A = [ [6.0, 0.0, -3.0, 0.0, 0.0],
      [3.0, -3.0, 0.0, 0.0, 0.0],
      [0.0, -1.0, 9.0, 0.0, 0.0],
      [0.0, 1.0, 8.0, -11.0, 2.0],
      [3.0, 1.0, 0.0, 0.0, -4.0]
     ]
b = [50.0, 0.0, 160.0, 0.0, 0.0]

gaussJordan(5, A, b)
