import math
import pylab as pl
class decay_A_and_B:
    def __init__(self,number_of_A=100,number_of_B=0,time_constant=1,time_of_duration=5,time_of_step=0.05):
        self.n_a = [number_of_A]
        self.n_b = [number_of_B]
        self.t=[0]
        self.tau = time_constant
        self.dt=time_of_step
        self.time=time_of_duration
        self.steps=int(time_of_duration//time_of_step+1)
        print("initial_number_of_A--->",number_of_A)
        print("initial_number_of_B--->",number_of_B)
        print("time_constant--------->",time_constant)
        print("total_time------------>",time_of_duration)
    def calcualtion(self):
        for i in range(self.steps):
            temp_A=self.n_a[i]+(self.n_b[i]-self.n_a[i])/self.tau*self.dt
            temp_B=self.n_b[i]+(self.n_a[i]-self.n_b[i])/self.tau*self.dt
            self.n_a.append(temp_A)
            self.n_b.append(temp_B)
            self.t.append(self.t[i]+self.dt)
    def show_result(self):
        plot_a,=pl.plot(self.t,self.n_a,"g")
        plot_b,=pl.plot(self.t,self.n_b,"r")
        pl.xlabel('time ($s$)')
        pl.ylabel('Number')
        pl.legend([plot_a, plot_b], ['A', 'B'],loc="best")
        pl.title('result of decay of two particles')
        pl.show()
    def store_results(self):
        myfile = open('data_of_problem1.5.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i],"   ", self.n_a[i],"  ",self.n_b[i], file = myfile)
        myfile.close()
a=decay_A_and_B()
a.calcualtion()
a.show_result()
a.store_results()  
