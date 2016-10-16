import pylab as pl
class cannon:
    def __init__(self, mass=1, time_step=0.1,total_time=86, initial_velocity=700,gg=9.8,BB2=4*10**(-5)):
        self.v = [initial_velocity]
        self.x = [0]
        self.vx = [420]
        self.y = [0]
        self.vy = [560]
        self.v1 = [initial_velocity]
        self.x1 = [0]
        self.vx1 = [420]
        self.y1 = [0]
        self.vy1 = [560]
        self.t = [0]
        self.g = gg
        self.B2 = BB2
        self.m = mass
        self.dt = time_step
        self.time = total_time   
    def run(self):
        _time = 0
        while(_time < self.time):
        #while(self.y >= 0):
            self.x.append(self.x[-1] +self.vx[-1]*self.dt)
            self.vx.append(self.vx[-1]-self.B2*self.v[-1]*self.vx[-1]/self.m*self.dt)                        
            self.y.append(self.y[-1] +self.vy[-1]*self.dt)                        
            self.vy.append(self.vy[-1]-self.g*self.dt-self.B2*self.v[-1]*self.vy[-1]/self.m*self.dt)         
            self.v.append((self.vx[-1]*self.vx[-1]+self.vy[-1]*self.vy[-1])**(1/2))
            
            self.x1.append(self.x1[-1] +self.vx1[-1]*self.dt)
            self.vx1.append(self.vx1[-1])                        
            self.y1.append(self.y1[-1] +self.vy1[-1]*self.dt)                        
            self.vy1.append(self.vy1[-1]-self.g*self.dt)         
            self.v1.append((self.vx1[-1]*self.vx1[-1]+self.vy1[-1]*self.vy1[-1])**(1/2))  
            
            self.t.append(_time)     
            _time += self.dt    
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.x, self.y)
        pl.plot(self.x1, self.y1)
        pl.title('Cannon shell', fontdict = font)
        pl.xlabel('x ($m$)')
        pl.ylabel('y ($m$)')
        pl.text(0.2 * self.time, 0.9 * self.v[-1],'', fontdict = font)
        pl.show()
        
a = cannon()
a.run()
a.show_results()


  