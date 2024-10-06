import router from "../utils/router.js"

const Register = {
    template : 
    `
    <div class="container">
        <div class="row m-5 no-gutters">
            <div class="col-md-6 d-none d-md-block">
                <img src="/static/media/communication-social-media-icons-smartphone-device.jpg" class="img-fluid" style="min-height:100%;" />
            </div>
            <div class="col-md-6 bg-white p-5">
                <h3 class="pb-3">Register</h3>
                <form>
                    <div class="row">
                        <div class="col">
                            <h4>  Select User Type:</h4>
                        </div>
                        <div class="col"> 
                            <input type="radio" class="btn-check" name="options-base" id="option2" value="sponsor" autocomplete="off" v-model="userType">
                            <label class="btn btn-outline-primary" for="option2">Sponsor</label>
                            <input type="radio" class="btn-check" name="options-base" id="option3" value="influencer" autocomplete="off" v-model="userType">
                            <label class="btn btn-outline-primary" for="option3">Influencer</label>
                        </div>
                    </div>
                    <div class="mb-3">
                        <label for="UserName" class="form-label">Username </label>
                        <input v-model="username" type="text" class="form-control" id="UserName">
                    </div>
                    <div class="mb-3">
                        <label for="InputEmail1" class="form-label">Email </label>
                        <input v-model="email" type="email" class="form-control" id="InputEmail1" aria-describedby="emailHelp">
                        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                    </div>
                    <div class="mb-3">
                        <label for="InputPassword1" class="form-label">Password</label>
                        <input v-model="password" type="password" class="form-control" id="InputPassword1">
                    </div>
                    <div class="pb-2">
                        <button type="Submit" class="btn btn-dark w-100 font-weight-bold mt-2">Register</button>
                    </div>
                </form>
                <div class="sideline">OR</div>
                <div style="text-align:center;">
                    <h6>Already have an account?</h6>
                    <router-link class="btn btn-primary w-100 font-weight-bold mt-2" to="/login">Login</router-link>
                </div>
            </div>
        </div>
    </div>
    `,
    data() {
        return{
            username:"",
            email:"",
            password:"",
            userType:"",
        }
    },
    methods: {
        async submitInfo() {
            const origin = window.location.origin;
            const url = `${origin}/login`;
            const res = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({email: this.email, password: this.password}),
                credentials: "same-origin",
            });

        }
    }
}

export default Register