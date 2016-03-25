# LaTeX2HTML 2008 (1.71)
# Associate images original text with physical files.


$key = q/{lstlisting}[language=Matlab]x=MX.sym('x',2,2);y=MX.sym('y');f=3*x+y;disp(f)disp(size(f)){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="219" HEIGHT="112" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img23.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = MX.sym('x',2,2);
y = MX.sym('y');
f = 3*x + y;
disp(f)
disp(size(f))
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]printM[0,[0,3]],M[[5,-6]]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="296" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img45.png"
 ALT="\begin{lstlisting}[language=Python]
print M[0,[0,3]], M[[5,-6]]
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=SX.sym('x',2)y=SX.sym('y')f=Function('f',[x,y],[x,sin(y)*x]){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="266" HEIGHT="111" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img95.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{subequations}{align}dot{h}&=v,qquad&h(0)=0dot{v}&=(u-a,v^2)slashm-g,qquad&v(0)=0dot{m}&=-b,u^2,qquad&m(0)=1{align}{subequations};MSF=1.6;LFS=12;TAGS=R;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="556" HEIGHT="91" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img203.png"
 ALT="\begin{subequations}\begin{align}\dot{h} &amp;= v, \qquad &amp;h(0) = 0 \ \dot{v} &amp;= (u...
...v(0) = 0 \ \dot{m} &amp;= -b   u^2, \qquad &amp;m(0) = 1 \end{align}\end{subequations}">|; 

$key = q/texttt{ncol}+1;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="76" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img175.png"
 ALT="$ \texttt{ncol}+1$">|; 

$key = q/{lstlisting}[language=Matlab]v=SX.sym('v',2);f=A*x;jtimes(f,x,v){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="197" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img91.png"
 ALT="\begin{lstlisting}[language=Matlab]
v = SX.sym('v',2);
f = A*x;
jtimes(f,x,v)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=SX.sym('x');y=SX.sym('y');z=SX.sym('z')nlp:x**2+100*z**2,'g':z+(1-x)**2-y}S=nlpsol('S','ipopt',nlp){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="704" HEIGHT="88" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img137.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=SX.sym('x');y=SX.sym('y')qp={'x':vertcat(x,y),'f':x**2+y**2,'g':x+y-10}S=qpsol('S','qpoases',qp){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="559" HEIGHT="88" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img145.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/f(x,p);MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="59" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img142.png"
 ALT="$ f(x,p)$">|; 

$key = q/{lstlisting}[language=Python]w=[x[0:3,:],x[3:5,:]]printw[0],w[1]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="264" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img67.png"
 ALT="\begin{lstlisting}[language=Python]
w = [x[0:3,:], x[3:5,:]]
print w[0], w[1]
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=C++]#include"casadislashcasadi.hpp"usingnamespacecasadi;cl:vector<DM>&arg){DMx=arg.at(0);DMf=sin(d*x);return{f};}};{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="673" HEIGHT="712" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img187.png"
 ALT="\begin{lstlisting}[language=C++]
...">|; 

$key = q/{lstlisting}[language=Matlab]M=SX([3789;4561]);disp(M){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="301" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img44.png"
 ALT="\begin{lstlisting}[language=Matlab]
M = SX([3 7 8 9; 4 5 6 1]);
disp(M)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]f=external('f','.slashff.so');disp(f(3.14)){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="320" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img166.png"
 ALT="\begin{lstlisting}[language=Matlab]
f = external('f', './ff.so');
disp(f(3.14))
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]y=SX.sym('y',10,1);size(y){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="231" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img74.png"
 ALT="\begin{lstlisting}[language=Matlab]
y = SX.sym('y',10,1);
size(y)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]f=MyCallback('f',0.5);res=f(2);disp(res){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="275" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img186.png"
 ALT="\begin{lstlisting}[language=Matlab]
f = MyCallback('f', 0.5);
res = f(2);
disp(res)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]x=MX.sym('x',2,2);x(1,1){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="219" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img25.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = MX.sym('x',2,2);
x(1,1)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]x=SX.sym('x',5,2)w=horzsplit(x,[0,1,2])printw[0],w[1]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="266" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img63.png"
 ALT="\begin{lstlisting}[language=Python]
x = SX.sym('x',5,2)
w = horzsplit(x,[0,1,2])
print w[0], w[1]
\end{lstlisting}">|; 

$key = q/displaystylebar{x}=left(frac{partialf}{partialx}right)^{text{T}},bar{y}.;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="126" HEIGHT="73" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img81.png"
 ALT="$\displaystyle \bar{x} = \left(\frac{\partial f}{\partial x}\right)^{\text{T}}   \bar{y}.$">|; 

$key = q/texttt{nnz}netexttt{nrow}*texttt{ncol};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="156" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img179.png"
 ALT="$ \texttt{nnz} \ne \texttt{nrow}*\texttt{ncol}$">|; 

$key = q/g;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="14" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img115.png"
 ALT="$ g$">|; 

$key = q/{lstlisting}[language=Matlab]C=DM(2,3);{par{C_dense=full(C);{par{C_sparse=sparse(C);{par{{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="231" HEIGHT="135" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img16.png"
 ALT="\begin{lstlisting}[language=Matlab]
C = DM(2,3);
\par
C_dense = full(C);
\par
C_sparse = sparse(C);
\par
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonr=S(x0=[2.5,3.0,0.75],lbg=0,ubg=0)x_opt=r['x']print'x_opt:',x_opt{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="277" HEIGHT="110" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img140.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=MX.sym('x',2)y=MX.sym('y')f=Function('f',[x,y],[x,sin(y)*x],['x','y'],['r','q'])f.generate('gen.c'){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="287" HEIGHT="157" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img158.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]printhorzcat(x,y){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="197" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img57.png"
 ALT="\begin{lstlisting}[language=Python]
print horzcat(x,y)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]disp(M(2:end,2:2:4)){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="219" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img42.png"
 ALT="\begin{lstlisting}[language=Matlab]
disp(M(2:end,2:2:4))
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]f=x^2+10;f=sqrt(f);display(f){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="139" HEIGHT="65" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img8.png"
 ALT="\begin{lstlisting}[language=Matlab]
f = x^2 + 10;
f = sqrt(f);
display(f)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]y=SX.sym('y',10,1)printy.shape{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="220" HEIGHT="42" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img73.png"
 ALT="\begin{lstlisting}[language=Python]
y = SX.sym('y',10,1)
print y.shape
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=MX.sym('x',2)y=MX.sym('y')f=Function('f',[x,y],[x,sin(y)*x],['x','y'],['r','q']){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="287" HEIGHT="134" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img100.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=C]intfname_work(int*sz_arg,int*sz_res,int*sz_iw,int*sz_w);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="711" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img181.png"
 ALT="\begin{lstlisting}[language=C]
int fname_work(int* sz_arg, int* sz_res, int* sz_iw, int* sz_w);
\end{lstlisting}">|; 

$key = q/displaystylehat{y}=frac{partialf}{partialx},hat{x}.;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="85" HEIGHT="61" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img80.png"
 ALT="$\displaystyle \hat{y} = \frac{\partial f}{\partial x}   \hat{x}.$">|; 

$key = q/{lstlisting}[language=Matlab]y=SX.sym('y',5);Z=SX.sym('Z',4,2);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="219" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img6.png"
 ALT="\begin{lstlisting}[language=Matlab]
y = SX.sym('y',5);
Z = SX.sym('Z',4,2);
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=C]slash*CASADIMETA:fname_N_IN1:fname_N_OUT2:fname_NAME_IN[OUT[0]r:fname_NAME_OUT[1]s:fname_SPARSITY_IN[0]2102*slash{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="325" HEIGHT="181" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img189.png"
 ALT="\begin{lstlisting}[language=C]
/*CASADIMETA
:fname_N_IN 1
:fname_N_OUT 2
:fname_...
..._OUT[0] r
:fname_NAME_OUT[1] s
:fname_SPARSITY_IN[0] 2 1 0 2
*/
\end{lstlisting}">|; 

$key = q/T=10;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="62" HEIGHT="17" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img220.png"
 ALT="$ T=10$">|; 

$key = q/{lstlisting}[language=Matlab]A=SX.sym('A',3,2);x=SX.sym('x',2);jacobian(A*x,x){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="221" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img85.png"
 ALT="\begin{lstlisting}[language=Matlab]
A = SX.sym('A',3,2);
x = SX.sym('x',2);
jacobian(A*x,x)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]x=SX.eye(4)printreshape(x,2,8){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="219" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img53.png"
 ALT="\begin{lstlisting}[language=Python]
x = SX.eye(4)
print reshape(x,2,8)
\end{lstlisting}">|; 

$key = q/f:mathbb{R}^{2}timesmathbb{R}rightarrowmathbb{R}^{2}timesmathbb{R}^{2},quad(x,y)mapsto(x,sin(y)x);MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="378" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img97.png"
 ALT="$ f : \mathbb{R}^{2} \times \mathbb{R} \rightarrow \mathbb{R}^{2} \times \mathbb{R}^{2}, \quad (x,y) \mapsto (x,\sin(y) x)$">|; 

$key = q/pinmathbb{R}^{np};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="67" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img134.png"
 ALT="$ p \in \mathbb{R}^{np}$">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=MX.sym('x',2,2)printx[0,0]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="209" HEIGHT="65" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img24.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#PythonM=diag(SX([3,4,5,6]))printM{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="257" HEIGHT="64" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img33.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Matlab]M(1,1),M(2,1),M(end,end){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="291" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img36.png"
 ALT="\begin{lstlisting}[language=Matlab]
M(1,1), M(2,1), M(end,end)
\end{lstlisting}">|; 

$key = q/{displaymath}{array}{cc}{array}{c}text{minimize:}x,y,z{array}&x^2+100,z^2{array}{c}text{subjectto:}{array}&z+(1-x)^2-y=0{array}{displaymath};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="276" HEIGHT="87" BORDER="0"
 SRC="|."$dir".q|img136.png"
 ALT="\begin{displaymath}\begin{array}{cc} \begin{array}{c} \text{minimize:} \ x,y,z ...
...c} \text{subject to:} \end{array} &amp; z+(1-x)^2-y = 0 \end{array}\end{displaymath}">|; 

$key = q/{lstlisting}[language=C++]slashslashC++#include<casadislashcasadi.hpp>usingnamesx,2)+10;f=sqrt(f);std::cout<<"f:"<<f<<std::endl;return0;}{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="435" HEIGHT="274" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img15.png"
 ALT="\begin{lstlisting}[language=C++]
// C++
...">|; 

$key = q/{lstlisting}[language=Matlab]dae=DaeBuilder;a=dae.add_p('a');b=dae.add_p('b');u=,'m');dae.set_unit('v','mslashs');dae.set_unit('m','kg');{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="267" HEIGHT="434" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img207.png"
 ALT="\begin{lstlisting}[language=Matlab]
dae = DaeBuilder;
a = dae.add_p('a');
b = da...
...unit('h','m');
dae.set_unit('v','m/s');
dae.set_unit('m','kg');
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]fromzipfileimportZipFilesfile=ZipFile(jmu_name','r')mfile=sfile.extract('modelDescription.xml','.'){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="546" HEIGHT="65" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img209.png"
 ALT="\begin{lstlisting}[language=Python]
from zipfile import ZipFile
sfile = ZipFile(jmu_name','r')
mfile = sfile.extract('modelDescription.xml','.')
\end{lstlisting}">|; 

$key = q/x_1;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="23" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img111.png"
 ALT="$ x_1$">|; 

$key = q/xinmathbb{R}^{nx};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="69" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img133.png"
 ALT="$ x \in \mathbb{R}^{nx}$">|; 

$key = q/{lstlisting}[language=C]constchar*fname_name_in(intind);constchar*fname_name_out(intind);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="398" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img173.png"
 ALT="\begin{lstlisting}[language=C]
const char* fname_name_in(int ind);
const char* fname_name_out(int ind);
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]printM[1:,1:4:2]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="183" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img41.png"
 ALT="\begin{lstlisting}[language=Python]
print M[1:,1:4:2]
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]y'{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="18" HEIGHT="18" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img52.png"
 ALT="\begin{lstlisting}[language=Matlab]
y'
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]printM[5],M[-6]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="185" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img37.png"
 ALT="\begin{lstlisting}[language=Python]
print M[5], M[-6]
\end{lstlisting}">|; 

$key = q/{displaymath}{array}{lc}{array}{l}text{minimize:}x(cdot)inmathbb{R}^2,,u(cdot)in{for0letleT}x_0(0)=0,quadx_1(0)=1,{array}{array}{displaymath};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="404" HEIGHT="227" BORDER="0"
 SRC="|."$dir".q|img219.png"
 ALT="\begin{displaymath}\begin{array}{lc} \begin{array}{l} \text{minimize:} \ x(\cdo...
... t \le T$} \ x_0(0)=0, \quad x_1(0)=1, \end{array} \end{array}\end{displaymath}">|; 

$key = q/{lstlisting}[language=Matlab]w={x(1:3,:),x(4:5,:)};w{1},w{2}{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="277" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img68.png"
 ALT="\begin{lstlisting}[language=Matlab]
w = {x(1:3,:), x(4:5,:)};
w{1}, w{2}
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonf=Function('f',[x],[sin(x)])opts=dict(main=True,mex=True)f.generate('ff.c',opts){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="332" HEIGHT="111" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img162.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/texttt{colind}[i];MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="80" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img176.png"
 ALT="$ \texttt{colind}[i]$">|; 

$key = q/{lstlisting}[language=C++]intmain(){Functionf=MyCallback::create("f",0.5);std::v:vector<DM>res=f(arg);std::cout<<res<<std::endl;return0;}{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="487" HEIGHT="158" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img188.png"
 ALT="\begin{lstlisting}[language=C++]
int main() {
Function f = MyCallback::create('...
...&lt;DM&gt; res = f(arg);
std::cout &#171; res &#171; std::endl;
return 0;
}
\end{lstlisting}">|; 

$key = q/dot{s};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="13" HEIGHT="17" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img194.png"
 ALT="$ \dot{s}$">|; 

$key = q/{lstlisting}[language=Matlab][H,g]=hessian(dot(x,x),x);display(H){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="307" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img89.png"
 ALT="\begin{lstlisting}[language=Matlab]
[H,g] = hessian(dot(x,x),x);
display(H)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]dae.add_lc('gamma,{'ode'});hes=dae.create(’hes’,...{'x','u','p','lam_ode'},...{'hes_gamma_x_x'});{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="330" HEIGHT="89" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img218.png"
 ALT="\begin{lstlisting}[language=Matlab]
dae.add_lc('gamma,{'ode'});
hes = dae.create(’hes’,...
{'x','u','p','lam_ode'},...
{'hes_gamma_x_x'});
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]sx_function=mx_function.expand(){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="374" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img108.png"
 ALT="\begin{lstlisting}[language=Python]
sx_function = mx_function.expand()
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]M=SX([3,7;4,5]);disp(M(1,:))M(1,:)=1;disp(M){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="200" HEIGHT="89" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img31.png"
 ALT="\begin{lstlisting}[language=Matlab]
M = SX([3,7;4,5]);
disp(M(1,:))
M(1,:) = 1;
disp(M)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]printgradient(dot(A,A),A){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="286" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img86.png"
 ALT="\begin{lstlisting}[language=Python]
print gradient(dot(A,A),A)
\end{lstlisting}">|; 

$key = q/g(x,p);MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="57" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img143.png"
 ALT="$ g(x,p)$">|; 

$key = q/{lstlisting}[language=Matlab]r=F('x0',0,'z0',0,'p',0.1);disp(r.xf){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="320" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img130.png"
 ALT="\begin{lstlisting}[language=Matlab]
r = F('x0',0,'z0',0,'p',0.1);
disp(r.xf)
\end{lstlisting}">|; 

$key = q/g_m;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="26" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img117.png"
 ALT="$ g_m$">|; 

$key = q/A;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="19" HEIGHT="16" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img153.png"
 ALT="$ A$">|; 

$key = q/dot{x}=;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="35" HEIGHT="17" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img198.png"
 ALT="$ \dot{x} =$">|; 

$key = q/i;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="11" HEIGHT="17" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img60.png"
 ALT="$ i$">|; 

$key = q/{lstlisting}[language=Python]dae=DaeBuilder()ocp.parse_fmi('modelDescription.xml'){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="411" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img210.png"
 ALT="\begin{lstlisting}[language=Python]
dae = DaeBuilder()
ocp.parse_fmi('modelDescription.xml')
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#PythonM=SX([[3,7],[4,5]])printM[0,:]M[0,:]=1printM{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="234" HEIGHT="110" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img30.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]classMyCallback(Callback):def__init__(self,name,d,oricallydefeval(self,arg):x=arg[0]f=sin(self.d*x)return[f]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="435" HEIGHT="435" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img183.png"
 ALT="\begin{lstlisting}[language=Python]
class MyCallback(Callback):
def __init__(se...
...def eval(self, arg):
x = arg[0]
f = sin(self.d*x)
return [f]
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]A=SX.sym('A',3,2)x=SX.sym('x',2)printjacobian(mtimes(A,x),x){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="323" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img84.png"
 ALT="\begin{lstlisting}[language=Python]
A = SX.sym('A',3,2)
x = SX.sym('x',2)
print jacobian(mtimes(A,x),x)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=C]intfname_n_in(void);intfname_n_out(void);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="240" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img172.png"
 ALT="\begin{lstlisting}[language=C]
int fname_n_in(void);
int fname_n_out(void);
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]f=Function('f',{x},{sin(x)});g=Function('g',{x},{co;C=CodeGenerator();C.add(f);C.add(g);C.generate('gen.c');{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="343" HEIGHT="135" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img161.png"
 ALT="\begin{lstlisting}[language=Matlab]
f = Function('f',{x},{sin(x)});
g = Function...
...;
C = CodeGenerator();
C.add(f);
C.add(g);
C.generate('gen.c');
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]gradient(dot(A,A),A){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="220" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img87.png"
 ALT="\begin{lstlisting}[language=Matlab]
gradient(dot(A,A),A)
\end{lstlisting}">|; 

$key = q/mathbb{R}timesmathbb{R}rightarrowmathbb{R};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="99" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img20.png"
 ALT="$ \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}$">|; 

$key = q/n;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="16" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img9.png"
 ALT="$ n$">|; 

$key = q/q;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="14" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img195.png"
 ALT="$ q$">|; 

$key = q/{lstlisting}[language=Matlab]ocp.make_explicit();{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="219" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img212.png"
 ALT="\begin{lstlisting}[language=Matlab]
ocp.make_explicit();
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#PythonH=2*DM.eye(2)A=DM.ones(1,2)g=DM.zeros(2)lba=10.{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="177" HEIGHT="107" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img150.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/w;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="19" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img196.png"
 ALT="$ w$">|; 

$key = q/y_m;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="27" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img114.png"
 ALT="$ y_m$">|; 

$key = q/{lstlisting}[language=Python]printy.T{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="100" HEIGHT="18" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img51.png"
 ALT="\begin{lstlisting}[language=Python]
print y.T
\end{lstlisting}">|; 

$key = q/{displaymath}{array}{cc}{array}{c}text{minimize:}x,y{array}&x^2+y^2{array}{c}text{subjectto:}{array}&x+y-10ge0{array}{displaymath};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="231" HEIGHT="87" BORDER="0"
 SRC="|."$dir".q|img144.png"
 ALT="\begin{displaymath}\begin{array}{cc} \begin{array}{c} \text{minimize:} \ x,y \e...
...y}{c} \text{subject to:} \end{array} &amp; x+y-10 \ge 0 \end{array}\end{displaymath}">|; 

$key = q/t;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="11" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img131.png"
 ALT="$ t$">|; 

$key = q/{lstlisting}[language=Matlab]r=S('lbg',0);x_opt=r.x;display(x_opt){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="162" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img148.png"
 ALT="\begin{lstlisting}[language=Matlab]
r = S('lbg',0);
x_opt = r.x;
display(x_opt)
\end{lstlisting}">|; 

$key = q/textit{nrow}*textit{ncol};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="95" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img75.png"
 ALT="$ \textit{nrow} * \textit{ncol}$">|; 

$key = q/{lstlisting}[language=Python]#Pythonfromcasadiimport*{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="223" HEIGHT="41" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img1.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/p=0.1;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="63" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img127.png"
 ALT="$ p=0.1$">|; 

$key = q/{lstlisting}[language=C]constint*fname_sparsity_in(intind);constint*fname_sparsity_out(intind);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="432" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img174.png"
 ALT="\begin{lstlisting}[language=C]
const int* fname_sparsity_in(int ind);
const int* fname_sparsity_out(int ind);
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythondae=DaeBuilder()#Addinputexpressionsa=dae.ad'h','m')dae.set_unit('v','mslashs')dae.set_unit('m','kg'){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="314" HEIGHT="549" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img206.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythonz=SX.sym('x',nz)x=SX.sym('x',nx)g0=(anexpresg=Function('g',[z,x],[g0,g1])G=rootfinder('G','newton',g){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="344" HEIGHT="157" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img120.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/z;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="14" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img110.png"
 ALT="$ z$">|; 

$key = q/m;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="21" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img10.png"
 ALT="$ m$">|; 

$key = q/mathbb{R}^{n_1timesm_1}timesldotstimesmathbb{R}^{n_Ntimesm_N}rightarrowmathbb{R}^{p_1timesq_1}timesldotstimesmathbb{R}^{p_Mtimesq_M};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="413" HEIGHT="38" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img21.png"
 ALT="$ \mathbb{R}^{n_1 \times m_1} \times \ldots \times \mathbb{R}^{n_N \times m_N} \...
...ow \mathbb{R}^{p_1 \times q_1} \times \ldots \times \mathbb{R}^{p_M \times q_M}$">|; 

$key = q/<A,B>:=;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="102" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img69.png"
 ALT="$ &lt;A,B&gt; :=$">|; 

$key = q/textit{offset}[i]lec<textit{offset}[i+1];MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="216" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img62.png"
 ALT="$ \textit{offset}[i] \le c &lt; \textit{offset}[i+1]$">|; 

$key = q/{lstlisting}[language=Matlab]display(B4){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="117" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img13.png"
 ALT="\begin{lstlisting}[language=Matlab]
display(B4)
\end{lstlisting}">|; 

$key = q/n=m=1;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="92" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img119.png"
 ALT="$ n=m=1$">|; 

$key = q/v;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="14" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img14.png"
 ALT="$ v$">|; 

$key = q/texttt{colind}[i+1];MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="113" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img177.png"
 ALT="$ \texttt{colind}[i+1]$">|; 

$key = q/{lstlisting}[language=Matlab]disp(M(:,2)){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="129" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img40.png"
 ALT="\begin{lstlisting}[language=Matlab]
disp(M(:,2))
\end{lstlisting}">|; 

$key = q/x_n;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="24" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img112.png"
 ALT="$ x_n$">|; 

$key = q/{subequations}{align}dot{x}&=z+p,0&=z,cos(z)-x{align}{subequations};MSF=1.6;LFS=12;TAGS=R;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="556" HEIGHT="63" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img123.png"
 ALT="\begin{subequations}\begin{align}\dot{x} &amp;= z+p, \ 0 &amp;= z   \cos(z)-x \end{align}\end{subequations}">|; 

$key = q/{lstlisting}[language=Matlab]x=MX.sym('x');{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="174" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img4.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = MX.sym('x');
\end{lstlisting}">|; 

$key = q/00;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="23" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img11.png"
 ALT="$ 00$">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=MX.sym('x'){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="165" HEIGHT="42" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img3.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythondae.add_lc('gamma',['ode'])hes=dae.create('hes’,['x','u','p','lam_ode'],['hes_gamma_x_x']){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="300" HEIGHT="111" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img217.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Matlab]A=MX.sym('A',3,3);b=MX.sym('b',3);solve(A,b){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="221" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img77.png"
 ALT="\begin{lstlisting}[language=Matlab]
A = MX.sym('A',3,3);
b = MX.sym('b',3);
solve(A,b)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]x=SX.sym('x',2,2)printdot(x,x){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="208" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img71.png"
 ALT="\begin{lstlisting}[language=Python]
x = SX.sym('x',2,2)
print dot(x,x)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]x=MX.sym('x',2);y=MX.sym('y');f=Function('f',{x,y},...{x,sin(y)*x},...{'x','y'},{'r','q'});{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="298" HEIGHT="112" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img101.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = MX.sym('x',2);
y = MX.sym('y');
f = Function('f',{x,y},...
{x,sin(y)*x},...
{'x','y'},{'r','q'});
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]z=SX.sym('x',nz);x=SX.sym('x',nx);g0=(anexpressionoFunction('g',{z,x},{g0,g1});G=rootfinder('G','newton',g);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="356" HEIGHT="135" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img121.png"
 ALT="\begin{lstlisting}[language=Matlab]
z = SX.sym('x',nz);
x = SX.sym('x',nx);
g0 =...
... = Function('g',{z,x},{g0,g1});
G = rootfinder('G','newton',g);
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=SX.sym('x',2,2)y=SX.sym('y')f=3*x+yprintfprintf.shape{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="209" HEIGHT="133" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img17.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{displaymath}{array}{cc}{array}{c}text{minimize:}x{array}&frac{1}{2}x^text{T},H,}a_{text{lb}}le&A,x&lea_{text{ub}}{array}{array}{displaymath};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="266" HEIGHT="109" BORDER="0"
 SRC="|."$dir".q|img149.png"
 ALT="\begin{displaymath}\begin{array}{cc} \begin{array}{c} \text{minimize:} \ x \end...
...xt{lb}} \le &amp; A   x&amp; \le a_{\text{ub}} \end{array} \end{array}\end{displaymath}">|; 

$key = q/{lstlisting}[language=Python]#PythonC=Compiler('ff.c','clang')f=external('f',C);printf(3.14){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="311" HEIGHT="88" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img167.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythony=SX.sym('y',5)Z=SX.sym('Z',4,2){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="209" HEIGHT="65" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img5.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Matlab]arg={1.1,3.3};res=f.call(arg);display(res)arg=struct('x',1.1,'y',3.3);res=f.call(arg);display(res){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="330" HEIGHT="135" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img107.png"
 ALT="\begin{lstlisting}[language=Matlab]
arg = {1.1,3.3};
res = f.call(arg);
display(...
...
arg = struct('x',1.1,'y',3.3);
res = f.call(arg);
display(res)
\end{lstlisting}">|; 

$key = q/s;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="13" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img193.png"
 ALT="$ s$">|; 

$key = q/{lstlisting}[language=Matlab]mexff.c-largeArrayDimsdisp(ff('f',3.14)){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="267" HEIGHT="42" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img169.png"
 ALT="\begin{lstlisting}[language=Matlab]
mex ff.c -largeArrayDims
disp(ff('f', 3.14))
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]w=SX.sym('w',3)f=mtimes(A,x)printjtimes(f,x,w,True){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="267" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img92.png"
 ALT="\begin{lstlisting}[language=Python]
w = SX.sym('w',3)
f = mtimes(A,x)
print jtimes(f,x,w,True)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonprint'B4:',B4{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="168" HEIGHT="41" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img12.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Matlab]f=dae.create('f',...{'x','u','p'},{'jac_ode_x'});{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="239" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img216.png"
 ALT="\begin{lstlisting}[language=Matlab]
f = dae.create('f',...
{'x','u','p'},
{'jac_ode_x'});
\end{lstlisting}">|; 

$key = q/u;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="15" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img204.png"
 ALT="$ u$">|; 

$key = q/{lstlisting}[language=Python]A=MX.sym('A',3,3)b=MX.sym('b',3)printsolve(A,b){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="210" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img76.png"
 ALT="\begin{lstlisting}[language=Python]
A = MX.sym('A',3,3)
b = MX.sym('b',3)
print solve(A,b)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonf=dae.create('f',['x','u','p'],['jac_ode_x']){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="222" HEIGHT="88" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img215.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/mathbb{R}rightarrowmathbb{R};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="62" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img19.png"
 ALT="$ \mathbb{R} \rightarrow \mathbb{R}$">|; 

$key = q/z(0)=0;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="73" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img128.png"
 ALT="$ z(0)=0$">|; 

$key = q/{lstlisting}[language=Matlab]x=SX.sym('x',2,2);y=SX.sym('y');f=3*x+y;disp(f)disp(size(f)){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="219" HEIGHT="112" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img18.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = SX.sym('x',2,2);
y = SX.sym('y');
f = 3*x + y;
disp(f)
disp(size(f))
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonarg=[1.1,3.3]res=f.call(arg)print'res:',resarg={'x':1.1,'y':3.3}res=f.call(arg)print'res:',res{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="254" HEIGHT="156" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img106.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/(A,B)=sum_{i,j},A_{i,j},B_{i,j};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="181" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img70.png"
 ALT="$ (A   B) = \sum_{i,j}   A_{i,j}   B_{i,j}$">|; 

$key = q/{lstlisting}[language=Matlab]x=SX.sym('x',5,2);w=horzsplit(x,[0,1,2]);w{1},w{2}{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="277" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img64.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = SX.sym('x',5,2);
w = horzsplit(x,[0,1,2]);
w{1}, w{2}
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=sh]#Commandlineecho3.143.14>ff_in.txtgccff.c-off.slashfff<ff_in.txt>ff_out.txtcatff_out.txt{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="345" HEIGHT="107" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img170.png"
 ALT="\begin{lstlisting}[language=sh]
...">|; 

$key = q/x(0)=0;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="74" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img126.png"
 ALT="$ x(0)=0$">|; 

$key = q/{lstlisting}[language=Matlab]r=S('h',H,'g',g,...'a',A,'lba',lba);x_opt=r.x;display(x_opt){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="285" HEIGHT="89" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img157.png"
 ALT="\begin{lstlisting}[language=Matlab]
r = S('h', H, 'g', g,...
'a', A, 'lba', lba);
x_opt = r.x;
display(x_opt)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=MX.sym('x',2,2)y=MX.sym('y')f=3*x+yprintfprintf.shape{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="209" HEIGHT="133" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img22.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/M;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="25" HEIGHT="16" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img32.png"
 ALT="$ M$">|; 

$key = q/displaystyley=f(x),;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="81" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img79.png"
 ALT="$\displaystyle y = f(x),$">|; 

$key = q/H;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="22" HEIGHT="16" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img152.png"
 ALT="$ H$">|; 

$key = q/{lstlisting}[language=Python]printM[:,1]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="127" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img39.png"
 ALT="\begin{lstlisting}[language=Python]
print M[:,1]
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#PythonprintSX.sym('x',Sparsity.lower(3)){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="389" HEIGHT="42" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img28.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/n+1;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="48" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img59.png"
 ALT="$ n+1$">|; 

$key = q/{lstlisting}[language=Matlab][r0,q0]=f(1.1,3.3);display(r0)display(q0){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="239" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img103.png"
 ALT="\begin{lstlisting}[language=Matlab]
[r0, q0] = f(1.1,3.3);
display(r0)
display(q0)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]f=functionname(name,arguments,...,[options]){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="542" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img94.png"
 ALT="\begin{lstlisting}[language=Python]
f = functionname(name, arguments, ..., [options])
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]w=SX.sym('w',3);f=A*xjtimes(f,x,w,true){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="200" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img93.png"
 ALT="\begin{lstlisting}[language=Matlab]
w = SX.sym('w',3);
f = A*x
jtimes(f,x,w,true)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]frompymodelicaimportcompile_jmujmu_name=compile_jmuations':True,'generate_fmi_me_xml':False}){lstlisting};MSF=1.6;LFS=12;TAGS=R;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="704" HEIGHT="88" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img208.png"
 ALT="\begin{lstlisting}[language=Python]
from pymodelica import compile_jmu
jmu_name=...
...
{'generate_xml_equations':True, 'generate_fmi_me_xml':False})
\end{lstlisting}">|; 

$key = q/texttt{colind}[texttt{ncol}];MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="113" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img178.png"
 ALT="$ \texttt{colind}[\texttt{ncol}]$">|; 

$key = q/{lstlisting}[language=Matlab]x=MX.sym('x',2);A=MX(2,2);A(1,1)=x(1);A(2,2)=x(1)+x(2);display(A){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="210" HEIGHT="112" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img27.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = MX.sym('x',2);
A = MX(2,2);
A(1,1) = x(1);
A(2,2) = x(1)+x(2);
display(A)
\end{lstlisting}">|; 

$key = q/{displaymath}{array}{cc}{array}{c}text{minimize:}x{array}&f(x,p){array}{c}text{s{text{lb}}le&g(x,p)&leg_{text{ub}}{array}{array}{displaymath};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="291" HEIGHT="109" BORDER="0"
 SRC="|."$dir".q|img132.png"
 ALT="\begin{displaymath}\begin{array}{cc} \begin{array}{c} \text{minimize:} \ x \end...
...ext{lb}} \le &amp;g(x,p)&amp; \le g_{\text{ub}} \end{array} \end{array}\end{displaymath}">|; 

$key = q/{equation*}{aligned}&g_0(z,x_1,x_2,ldots,x_n)&&=0&g_1(z,x_1,x_2,ldots,x_n)&&=y_1ad&g_m(z,x_1,x_2,ldots,x_n)&&=y_m,{aligned}{equation*};MSF=1.6;LFS=12;TAGS=R;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="227" HEIGHT="161" BORDER="0"
 SRC="|."$dir".q|img109.png"
 ALT="\begin{equation*}\begin{aligned}&amp;g_0(z, x_1, x_2, \ldots, x_n) &amp;&amp;= 0 \ &amp;g_1(z, ...
...&amp;&amp;\qquad \ &amp;g_m(z, x_1, x_2, \ldots, x_n) &amp;&amp;= y_m, \end{aligned}\end{equation*}">|; 

$key = q/f:mathbb{R}^Nrightarrowmathbb{R}^M;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="117" HEIGHT="40" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img78.png"
 ALT="$ f: \mathbb{R}^N \rightarrow \mathbb{R}^M$">|; 

$key = q/{lstlisting}[language=Python]printy*y,mtimes(y,y){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="242" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img49.png"
 ALT="\begin{lstlisting}[language=Python]
print y*y, mtimes(y,y)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]x=SX.sym('x')y=SX.sym('y',2,2)printsin(y)-x{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="208" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img47.png"
 ALT="\begin{lstlisting}[language=Python]
x = SX.sym('x')
y = SX.sym('y',2,2)
print sin(y)-x
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]qp=struct;qp.h=H.sparsity();qp.a=A.sparsity();S=qpsol('S','qpoases',qp);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="309" HEIGHT="86" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img155.png"
 ALT="\begin{lstlisting}[language=Matlab]
qp = struct;
qp.h = H.sparsity();
qp.a = A.sparsity();
S = qpsol('S','qpoases',qp);
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonr=S(h=H,g=g,a=A,lba=lba)x_opt=r['x']print'x_opt:',x_opt{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="244" HEIGHT="110" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img156.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythonf=dae.create('f',['x','u','p'],['ode']){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="298" HEIGHT="65" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img213.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythonocp.make_explicit(){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="209" HEIGHT="42" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img211.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/y_1;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="21" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img113.png"
 ALT="$ y_1$">|; 

$key = q/{lstlisting}[language=Matlab]res=f('x',1.1,'y',3.3);display(res){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="273" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img105.png"
 ALT="\begin{lstlisting}[language=Matlab]
res = f('x',1.1,'y',3.3);
display(res)
\end{lstlisting}">|; 

$key = q/dot{q}=;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="33" HEIGHT="34" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img202.png"
 ALT="$ \dot{q} =$">|; 

$key = q/{lstlisting}[language=C]voidfname_simple(constdouble*arg,double*res);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="555" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img190.png"
 ALT="\begin{lstlisting}[language=C]
void fname_simple(const double* arg, double* res);
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=SX.sym('x');z=SX.sym('z');p=SX.sym('p')daep,'ode':z+p,'alg':z*cos(z)-x}F=integrator('F','idas',dae){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="626" HEIGHT="88" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img124.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=MX.sym('x',2)A=MX(2,2)A[0,0]=x[0]A[1,1]=x[0]+x[1]print'A:',A{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="197" HEIGHT="133" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img26.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/d;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="14" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img192.png"
 ALT="$ d$">|; 

$key = q/{lstlisting}[language=Matlab]x=SX.sym('x');z=SX.sym('z');p=SX.sym('p');dae=struc'ode',z+p,'alg',z*cos(z)-x);F=integrator('F','idas',dae);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="657" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img125.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = SX.sym('x'); z = SX.sym('z'); p = SX.sym...
...,'ode',z+p,'alg',z*cos(z)-x);
F = integrator('F', 'idas', dae);
\end{lstlisting}">|; 

$key = q/(t,w,x,s,z,u,p,d,dot{s})=0;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="209" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img200.png"
 ALT="$ (t,w,x,s,z,u,p,d,\dot{s}) =0$">|; 

$key = q/{lstlisting}[language=Matlab]x=SX.sym('x',2,2)dot(x,x){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="208" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img72.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = SX.sym('x',2,2)
dot(x,x)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]x=SX.sym('x',5)y=SX.sym('y',5)printvertcat(x,y){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="198" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img55.png"
 ALT="\begin{lstlisting}[language=Python]
x = SX.sym('x',5)
y = SX.sym('y',5)
print vertcat(x,y)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]M=diag(SX([3,4,5,6]));disp(M){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="268" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img34.png"
 ALT="\begin{lstlisting}[language=Matlab]
M = diag(SX([3,4,5,6]));
disp(M)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=C]voidfname_incref(void);voidfname_decref(void);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="264" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img171.png"
 ALT="\begin{lstlisting}[language=C]
void fname_incref(void);
void fname_decref(void);
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]f=Function('f',{x},{sin(x)});opts=struct('main',true,...'mex',true);f.generate('ff.c',opts);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="341" HEIGHT="89" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img163.png"
 ALT="\begin{lstlisting}[language=Matlab]
f = Function('f',{x},{sin(x)});
opts = struct('main', true,...
'mex', true);
f.generate('ff.c',opts);
\end{lstlisting}">|; 

$key = q/L(x,lambda)=f(x)+lambda^{text{T}},g(x));MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="213" HEIGHT="40" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img135.png"
 ALT="$ L(x,\lambda) = f(x) + \lambda^{\text{T}}   g(x))$">|; 

$key = q/{lstlisting}[language=Python]w=vertsplit(x,[0,3,5])printw[0],w[1]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="266" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img65.png"
 ALT="\begin{lstlisting}[language=Python]
w = vertsplit(x,[0,3,5])
print w[0], w[1]
\end{lstlisting}">|; 

$key = q/[2.5,3.0,0.75];MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="113" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img139.png"
 ALT="$ [2.5,3.0,0.75]$">|; 

$key = q/g_0;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="21" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img116.png"
 ALT="$ g_0$">|; 

$key = q/{lstlisting}[language=Matlab]disp(SX.sym('x',Sparsity.lower(3))){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="387" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img29.png"
 ALT="\begin{lstlisting}[language=Matlab]
disp(SX.sym('x',Sparsity.lower(3)))
\end{lstlisting}">|; 

$key = q/p;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="14" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img191.png"
 ALT="$ p$">|; 

$key = q/y;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="14" HEIGHT="35" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img197.png"
 ALT="$ y$">|; 

$key = q/{lstlisting}[language=Matlab]C=Compiler('ff.c','clang');f=external('f',C);disp(f(3.14)){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="321" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img168.png"
 ALT="\begin{lstlisting}[language=Matlab]
C = Compiler('ff.c','clang');
f = external('f',C);
disp(f(3.14))
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]x=SX.sym('x',2);y=SX.sym('y');f=Function('f',{x,y},...{x,sin(y)*x});{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="286" HEIGHT="89" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img96.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = SX.sym('x',2);
y = SX.sym('y');
f = Function('f',{x,y},...
{x,sin(y)*x});
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonr=F(x0=0,z0=0,p=0.1)printr['xf']{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="266" HEIGHT="65" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img129.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Matlab]importcasadi.*{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="163" HEIGHT="18" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img2.png"
 ALT="\begin{lstlisting}[language=Matlab]
import casadi.*
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]v=SX.sym('v',2)f=mtimes(A,x)printjtimes(f,x,v){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="209" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img90.png"
 ALT="\begin{lstlisting}[language=Python]
v = SX.sym('v',2)
f = mtimes(A,x)
print jtimes(f,x,v)
\end{lstlisting}">|; 

$key = q/(t,w,x,s,z,u,p,d)=0;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="192" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img201.png"
 ALT="$ (t,w,x,s,z,u,p,d) = 0$">|; 

$key = q/{lstlisting}[language=Matlab]x=SX.sym('x',5);y=SX.sym('y',5);[x;y]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="197" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img56.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = SX.sym('x',5);
y = SX.sym('y',5);
[x;y]
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]x=SX.sym('x');y=SX.sym('y')qp=struct('x',[x;y],'f':x^2+y^2,'g',x+y-10)S=qpsol('S','qpoases',qp){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="524" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img146.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = SX.sym('x'); y = SX.sym('y')
qp = struct('x',[x;y], 'f':x^2+y^2, 'g',x+y-10)
S = qpsol('S', 'qpoases', qp)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]x=SX.eye(4);reshape(x,2,8){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="152" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img54.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = SX.eye(4);
reshape(x,2,8)
\end{lstlisting}">|; 

$key = q/c;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="13" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img61.png"
 ALT="$ c$">|; 

$key = q/{lstlisting}[language=Matlab]y.*y,y*y{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="99" HEIGHT="13" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img50.png"
 ALT="\begin{lstlisting}[language=Matlab]
y.*y, y*y
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=sh]gcc-fPIC-sharedgen.c-ogen.so{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="366" HEIGHT="18" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img164.png"
 ALT="\begin{lstlisting}[language=sh]
gcc -fPIC -shared gen.c -o gen.so
\end{lstlisting}">|; 

$key = q/(a,b);MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="45" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img205.png"
 ALT="$ (a,b)$">|; 

$key = q/x;MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="15" HEIGHT="19" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img83.png"
 ALT="$ x$">|; 

$key = q/{lstlisting}[language=Matlab]x=SX.sym('x');y=SX.sym('y');z=SX.sym('z');nlp=struc'f':x^2+100*z^2,'g',z+(1-x)^2-y)S=nlpsol('S','ipopt',nlp){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="658" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img138.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = SX.sym('x'); y = SX.sym('y'); z = SX.sym...
...'f':x^2+100*z^2, 'g',z+(1-x)^2-y)
S = nlpsol('S', 'ipopt', nlp)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab][x,y]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="46" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img58.png"
 ALT="\begin{lstlisting}[language=Matlab]
[x,y]
\end{lstlisting}">|; 

$key = q/G:{z_{text{guess}},x_1,x_2,ldots,x_n}rightarrow{z,y_1,y_2,ldots,y_m};MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="382" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img118.png"
 ALT="$ G: \{z_{\text{guess}}, x_1, x_2, \ldots, x_n\} \rightarrow \{z, y_1, y_2, \ldots, y_m\}$">|; 

$key = q/{lstlisting}[language=Python]M=SX([[3,7,8,9],[4,5,6,1]])printM{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="324" HEIGHT="42" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img43.png"
 ALT="\begin{lstlisting}[language=Python]
M = SX([[3,7,8,9],[4,5,6,1]])
print M
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]M(1,[1,4]),M([6,numel(M)-5]){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="325" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img46.png"
 ALT="\begin{lstlisting}[language=Matlab]
M(1,[1,4]), M([6,numel(M)-5])
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonr=S(lbg=0)x_opt=r['x']print'x_opt:',x_opt{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="244" HEIGHT="87" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img147.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/f(x);MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="41" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img82.png"
 ALT="$ f(x)$">|; 

$key = q/{lstlisting}[language=Python]#Pythonf=Function('f',[x],[sin(x)])g=Function('g',[(x)])C=CodeGenerator()C.add(f)C.add(g)C.generate('gen.c'){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="332" HEIGHT="157" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img160.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythonqp={}qp['h']=H.sparsity()qp['a']=A.sparsity()S=qpsol('S','qpoases',qp){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="300" HEIGHT="111" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img154.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Matlab]w=vertsplit(x,[0,3,5]);w{1},w{2}{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="277" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img66.png"
 ALT="\begin{lstlisting}[language=Matlab]
w = vertsplit(x,[0,3,5]);
w{1}, w{2}
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=C]intfname(constdouble**arg,double**res,int*iw,double*w,intmem);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="476" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img182.png"
 ALT="\begin{lstlisting}[language=C]
int fname(const double** arg, double** res,
int* iw, double* w, int mem);
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python][H,g]=hessian(dot(x,x),x)print'H:',H{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="298" HEIGHT="42" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img88.png"
 ALT="\begin{lstlisting}[language=Python]
[H,g] = hessian(dot(x,x),x)
print 'H:', H
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]x=SX.sym('x');y=SX.sym('y',2,2);sin(y)-x{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="219" HEIGHT="66" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img48.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = SX.sym('x');
y = SX.sym('y',2,2);
sin(y)-x
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]f=dae.create('f',...{'x','u','p'},{'ode'});{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="307" HEIGHT="43" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img214.png"
 ALT="\begin{lstlisting}[language=Matlab]
f = dae.create('f',...
{'x','u','p'},{'ode'});
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonr0,q0=f(1.1,3.3)print'r0:',r0print'q0:',q0{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="209" HEIGHT="87" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img102.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Matlab]M(6),M(end-5){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="158" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img38.png"
 ALT="\begin{lstlisting}[language=Matlab]
M(6), M(end-5)
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]H=2*DM.eye(2);A=DM.ones(1,2);g=DM.zeros(2);lba=10;{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="188" HEIGHT="88" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img151.png"
 ALT="\begin{lstlisting}[language=Matlab]
H = 2*DM.eye(2);
A = DM.ones(1,2);
g = DM.zeros(2);
lba = 10;
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=C]intfname_n_mem(void);{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="240" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img180.png"
 ALT="\begin{lstlisting}[language=C]
int fname_n_mem(void);
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]x=MX.sym('x',2);y=MX.sym('y');f=Function('f',{x,y},...{x,sin(y)*x});{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="298" HEIGHT="89" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img99.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = MX.sym('x',2);
y = MX.sym('y');
f = Function('f',{x,y},...
{x,sin(y)*x});
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Python]#Pythonf=x**2+10f=sqrt(f)print'f:',f{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="144" HEIGHT="87" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img7.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythonf=external('f','.slashff.so')printf(3.14){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="311" HEIGHT="65" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img165.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythonres=f(x=1.1,y=3.3)print'res:',res{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="233" HEIGHT="64" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img104.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Usethefunctionf=MyCallback('f',0.5)res=f(2)printres{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="265" HEIGHT="87" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img184.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Python]#Pythonx=MX.sym('x',2)y=MX.sym('y')f=Function('f',[x,y],[x,sin(y)*x]){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="287" HEIGHT="111" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img98.png"
 ALT="\begin{lstlisting}[language=Python]
...">|; 

$key = q/{lstlisting}[language=Matlab]r=S('x0',[2.5,3.0,0.75],...'lbg',0,'ubg',0);x_opt=r.x;display(x_opt){lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="319" HEIGHT="89" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img141.png"
 ALT="\begin{lstlisting}[language=Matlab]
r = S('x0',[2.5,3.0,0.75],...
'lbg',0,'ubg',0);
x_opt = r.x;
display(x_opt)
\end{lstlisting}">|; 

$key = q/(t,w,x,s,z,u,p,d);MSF=1.6;LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="157" HEIGHT="39" ALIGN="MIDDLE" BORDER="0"
 SRC="|."$dir".q|img199.png"
 ALT="$ (t,w,x,s,z,u,p,d)$">|; 

$key = q/{subequations}{align}dot{x}&=f_{text{ode}}(t,x,z,p),qquadx(0)=x_00&=f_{text{alg}{text{quad}}(t,x,z,p),qquadq(0)=0{align}{subequations};MSF=1.6;LFS=12;TAGS=R;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="556" HEIGHT="91" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img122.png"
 ALT="\begin{subequations}\begin{align}\dot{x} &amp;= f_{\text{ode}}(t,x,z,p), \qquad x(0)...
...ot{q} &amp;= f_{\text{quad}}(t,x,z,p), \qquad q(0) = 0 \end{align}\end{subequations}">|; 

$key = q/{lstlisting}[language=Python]printM[0,0],M[1,0],M[-1,-1]{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="331" HEIGHT="20" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img35.png"
 ALT="\begin{lstlisting}[language=Python]
print M[0,0], M[1,0], M[-1,-1]
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]x=MX.sym('x',2);y=MX.sym('y');f=Function('f',{x,y},{x,sin(y)*x},...{'x','y'},{'r','q'});f.generate('gen.c');{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="298" HEIGHT="135" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img159.png"
 ALT="\begin{lstlisting}[language=Matlab]
x = MX.sym('x',2);
y = MX.sym('y');
f = Func...
....
{x,sin(y)*x},...
{'x','y'},{'r','q'});
f.generate('gen.c');
\end{lstlisting}">|; 

$key = q/{lstlisting}[language=Matlab]classdefMyCallback<casadi.Callbackpropertiesdendmet=eval(self,arg)x=arg{1};f=sin(self.d*x);arg={f};endendend{lstlisting};LFS=12;AAT/;
$cached_env_img{$key} = q|<IMG
 WIDTH="456" HEIGHT="660" ALIGN="BOTTOM" BORDER="0"
 SRC="|."$dir".q|img185.png"
 ALT="\begin{lstlisting}[language=Matlab]
classdef MyCallback &lt; casadi.Callback
prop...
...)
x = arg{1};
f = sin(self.d * x);
arg = {f};
end
end
end
\end{lstlisting}">|; 

1;

