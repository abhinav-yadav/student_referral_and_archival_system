package javabeans;

import java.io.*;
public class LoginBean implements Serializable
{
private String username;
private String password;
public LoginBean(){
}
public void setUsername(String un){
this.username=un;
}
public String getUsername(){
return username;
}
public void setPassword(String pwd){
this.password=pwd;
}
public String getPassword(){
return password;
}
public int Verify(){
if(username.equals("abhi")&&password.equals("7989"))
return 1;
else
return 0;
}}