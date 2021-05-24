package javabeans;
import java.io.*;
import javabeans.LoginBean;
public class Authenticate{
public static void main(String args[]) throws Exception {
LoginBean lb=new LoginBean();
String uname;
String pwd;
DataInputStream din=new DataInputStream(System.in);
System.out.println("Enter Username");
uname=din.readLine();
System.out.println("Enter password");
pwd=din.readLine();
lb.setUsername(uname);
lb.setPassword(pwd);
if(lb.Verify()==1)
System.out.println("Authorized user");
else
System.out.println("not authorized");
}}