import numpy as np
from numpy import linalg as LA
import math
import matplotlib.pyplot as plt


A = np.array(
	[
		[0, 3, 0, 0],
		[1, 0, 0, -1/6],
		[0, 0, 0, -1],
		[0, -4, -3, 0],
	])

wa, va = LA.eig(A)
print(wa, va, sep = '\n\n')

# lambda1 = wa[0]
# lambda2 = wa[1]
# lambda3 = wa[2]
# lambda4 = wa[3]
#
# K = np.array(va).transpose()
# K = np.array(va)

lambda1 = (-math.sqrt(6)+math.sqrt(114))/6
lambda2 = (math.sqrt(6)-math.sqrt(114))/6
lambda3 = (math.sqrt(6)+math.sqrt(114))/6
lambda4 = (-math.sqrt(6)-math.sqrt(114))/6

K = np.array(
	[
		[(math.sqrt(19)+1)/12			  , (math.sqrt(19)+1)/12			, (-math.sqrt(19)+1)/12			  , (-math.sqrt(19)+1)/12],
		[math.sqrt(6)/12 	 			  , -math.sqrt(6)/12				, -math.sqrt(6)/12				  , math.sqrt(6)/12],
		[(-math.sqrt(6)-math.sqrt(114))/18, (math.sqrt(6)+math.sqrt(114))/18, (math.sqrt(6)-math.sqrt(114))/18, (-math.sqrt(6)+math.sqrt(114))/18],
		[1					 			  , 1								, 1								  , 1]
	])

K_inv = LA.inv(K)





def matr_e(t, t0):
	matrix = np.array(
		[
			[math.exp(lambda1*(t-t0)), 	0, 							0, 							0						],
			[0, 						math.exp(lambda2*(t-t0)), 	0, 							0						],
			[0, 						0, 							math.exp(lambda3*(t-t0)), 	0						],
			[0, 						0, 							0, 							math.exp(lambda4*(t-t0))],
		])

	return matrix


def find_K_matrix(t, t0, K, K_inv):
	F = np.dot(K.dot(matr_e(t, t0)), K_inv)


	Fi_11 = np.array(
			[
				[F[0,0], F[0,1]],
				[F[1,0], F[1,1]],
			])

	Fi_12 = np.array(
			[
				[F[0,2], F[0,3]],
				[F[1,2], F[1,3]],
			])

	Fi_21 = np.array(
			[
				[F[2,0], F[2,1]],
				[F[3,0], F[3,1]],
			])

	Fi_22 = np.array(
			[
				[F[2,2], F[2,3]],
				[F[3,2], F[3,3]],
			])



	delta = np.array(
		[
			[1, 0],
			[0, 2]
		])

	K = 0.5 * np.dot(LA.inv(Fi_22 - 2 * delta.dot(Fi_12)), Fi_21 - 2 * delta.dot(Fi_11))
	return K


def find_X_and_U(t, t0, K, K_inv, K_matrix):

	F = np.dot(K.dot(matr_e(t, t0)), K_inv)


	Fi_11 = np.array(
			[
				[F[0,0], F[0,1]],
				[F[1,0], F[1,1]],
			])

	Fi_12 = np.array(
			[
				[F[0,2], F[0,3]],
				[F[1,2], F[1,3]],
			])

	Fi_21 = np.array(
			[
				[F[2,0], F[2,1]],
				[F[3,0], F[3,1]],
			])

	Fi_22 = np.array(
			[
				[F[2,2], F[2,3]],
				[F[3,2], F[3,3]],
			])



	delta = np.array(
		[
			[1, 0],
			[0, 2]
		])

	# K = 0.5 * np.dot(LA.inv(Fi_22 - 2 * delta.dot(Fi_12)), Fi_21 - 2 * delta.dot(Fi_11))




	X0 = np.array([[1],[1]])

	X 	= (Fi_11 - 2*Fi_12.dot(K_matrix)).dot(X0)
	Psi = (Fi_21 - 2*Fi_22.dot(K_matrix)).dot(X0)
	print(Psi)
	input()
	u = -1/6*Psi[1]

	return (X, u)


X1 = []
X2 = []
U = []
T = []

t0 = 0
tk = 4
t = t0
dt = .01

while t < tk:
	result = find_X_and_U(t=t, t0=t0, K=K, K_inv=K_inv, K_matrix=find_K_matrix(t=4,t0=0,K=K,K_inv=K_inv))
	# print(result[0][0][0], result[0][1][0], result[1][0])

	X1.append(result[0][0][0])
	X2.append(result[0][1][0])
	U.append(result[1][0])
	T.append(t)
	t+=dt



# print(X1,X2,U,T,sep='\n\n\n')

plt.plot(T, X1, label='X1' )
plt.plot(T, X2, label = 'X2' )
plt.plot(T, U, label='u')
plt.legend()
plt.grid(True)
plt.savefig('./charts/part1.png')
plt.show()

