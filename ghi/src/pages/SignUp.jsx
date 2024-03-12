const SignUp = () => {
    const handleSubmit = (e) => {
        e.preventDefault()
        console.log('login')
    }
    return (
        <div className="row">
            <div className="col-md-6 offset-md-3">
                <h1>SignUp</h1>
                <form>
                    <div className="mb-3">
                        <label
                            htmlFor="SignUp__username"
                            className="form-label"
                        >
                            Username
                        </label>
                        <input
                            type="text"
                            className="form-control"
                            id="SignUp__username"
                        />
                    </div>
                    <div className="mb-3">
                        <label
                            htmlFor="SignUp__password"
                            className="form-label"
                        >
                            Password
                        </label>
                        <input
                            type="password"
                            className="form-control"
                            id="SignUp__password"
                        />
                    </div>
                    <div className="mb-3">
                        <label
                            htmlFor="SignUp__password_confirmation"
                            className="form-label"
                        >
                            Confirm Password
                        </label>
                        <input
                            type="password"
                            className="form-control"
                            id="SignUp__password_confirmation"
                        />
                    </div>
                    <button type="submit" className="btn btn-success">
                        Submit
                    </button>
                </form>
            </div>
        </div>
    )
}

export default SignUp
