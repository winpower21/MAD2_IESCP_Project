import router from "../utils/router.js"

const Login = {
    template : 
    `
    <div class="container">
        <div class="row m-5 no-gutters">
            <div class="col-md-6 d-none d-md-block">
                <img src="/static/media/communication-social-media-icons-smartphone-device.jpg" class="img-fluid" style="min-height:100%;" />
            </div>
            <div class="col-md-6 bg-white p-5">
                <h3 class="pb-3">Login</h3>
                <div>
                    <div class="mb-3">
                        <label for="InputEmail1" class="form-label">Email </label>
                        <input v-model="email" type="email" class="form-control" id="InputEmail1" aria-describedby="emailHelp">
                        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                    </div>
                    <div class="mb-3">
                        <label for="InputPassword1" class="form-label">Password</label>
                        <input v-model="password" type="password" class="form-control" id="InputPassword1">
                    </div>
                    <div class="row">
                        <div class="col" style="text-align: right;">
                            <a href="#">Forgot Password?</a>
                        </div>
                    </div>
                    <div>
                        <h5 class="text-center" style="color:red;">{{loginMessage}}</h5>
                    </div>
                    <div class="pb-2">
                        <button class="btn btn-dark w-100 font-weight-bold mt-2" @click="submitInfo">Submit</button>
                    </div>
                </div>
                <div class="sideline">OR</div>
                <div style="text-align:center;">
                    <h6>Don't have an account?</h6>
                    <router-link class="btn btn-primary w-100 font-weight-bold mt-2" to="/register">Register</router-link>
                </div>
            </div>
        </div>
    </div>
    `,
    data() {
        return{
            email:"",
            password:"",
            loginMessage:""
        }
    },
    methods: {
        async submitInfo() {
            const url = window.location.origin;
            const res = await fetch(url+'/login', {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({email: this.email, password: this.password}),
                credentials: "same-origin",
            });
            
            if (res.ok) {
                const data = await res.json();
                console.log(data.user, data.role)
                switch (data.role) {
                    case "Admin":
                        router.push("/admin-dash");
                        break;
                    case "Influencer":
                        router.push("/influencer-dash");
                        break;
                    case "Sponsor":
                        router.push("/sponsor-dash");
                        break;
                }
            } else {
                const errorData = await res.json();
                this.loginMessage = errorData.message;
                
            }
        }
    }
}

export default Login