import { executeQuery } from "../../database/database.js";
import * as bcrypt from "https://deno.land/x/bcrypt@v0.4.1/mod.ts";
import { renderFile } from "../../deps.js";
const showMain = ({ render }) => {
  render("login.eta");
};
const dashboard=async({render,state})=>{
  const data={
    id:"",
    name:"",
    drivers:""
  }
  data.id=await state.session.get("user_id");
  let name=await executeQuery("SELECT username FROM users WHERE id=$id",{id:data.id});
  let driver=await executeQuery("SELECT name,on_duty,trips FROM drivers WHERE employer_email=(SELECT email FROM users WHERE id=$id)",{id:data.id});
  console.log(driver);
  data.name=name.rows[0].username;
  data.drivers=driver.rows;
  render("dashboard.eta",data);
}
const login=async({render,request,response,state})=>{
  const data={
    message:""
  }
  const body = request.body();
  const params = await body.value;
  console.log(params.get("txt"));
  console.log(params.get("email"));
  console.log(params.get("pswd"));
  if (params.get("txt")!=null){
    await executeQuery("INSERT INTO users(username,email,passwords) VALUES ($username,$email,$password)",
    {username:params.get("txt"),email:params.get("email"),password:await bcrypt.hash(params.get("pswd"))});
    data.message="You are signed in! Please login now."
    render("login.eta",data);
  }
  else{
    let Email=params.get("email");
    let result= await executeQuery("SELECT * FROM users WHERE email=$email", {email:Email});
    console.log(result);
    if(result.rows.length != 1){
      data.message="First time? Login first."
      render("login.eta",data);
    }
    else{
      const compare=await bcrypt.compare(params.get("pswd"),result.rows[0].passwords);
      if(compare){
        await state.session.set("user", Email);
        await state.session.set("user_id",result.rows[0].id);
        response.redirect("/dash");
      }
      else{
        data.message="Email or password incorrect!";
        render("login.eta",data);
      }
    }
  }
}
const Driver_status=async({params,render})=>{
  const data={
    trips:"",
    name:""
  }
  let name=((params.name).replace('%','')).replace('20',' ');
  data.name=name;
  let trip=await executeQuery("SELECT * FROM trips WHERE name=$name",{name:name});
  data.trips=trip.rows;
  console.log(data.trips)
  render("status.eta",data);
  
}
export { showMain,dashboard,login,Driver_status };
