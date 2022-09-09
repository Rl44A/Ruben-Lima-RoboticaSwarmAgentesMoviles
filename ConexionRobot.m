% ip="192.168.50.200";
% Robotat=robotat_connect(ip)
continueRunning=true;
address1 = '192.168.50.167';
address2 = '192.168.50.165';
port = 2010;    
u=udp(address1,port);
fopen(u);
v=udp(address2,port);
fopen(v);
while(continueRunning)
% R1=robotat_get_pose(Robotat,1)
% R2=robotat_get_pose(Robotat,2)
R1=[2.25   -0.1665    2.9523    0.0392    0.2032    0.3613    0.9092];

R2=[2.2079   -0.1665    2.9523    0.5606    0.7891    0.0740    0.2400];%



indicador = 'T1,';
string1 = strcat(indicador, string(R1(1)), ','); 
string1 = strcat(string1, string(R1(3)),',');
string1 = strcat(string1, string(R1(4)));

indicador = 'T2,';
string2 = strcat(indicador, string(R2(1)), ',');
string2 = strcat(string2, string(R2(3)),',');
string2 = strcat(string2, string(R2(4)));



    fwrite(u,string1,"char");
    fwrite(v,string2,"char");
    pause(10);
    continueRunning = input('Continue? ');
    i=i+1;

end

data = fgetl(u);
data2 = fgetl(v);

disp(data);
disp(data2);