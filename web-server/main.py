import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def get_home():
    return """
        <html>
            <head>
                <title>Welcome to my site!</title>
                <style>
                    body {
                        background-color: #ffa8ff;
                        margin: 0;
                        padding: 0;
                        font-family: "Pacifico", cursive;
                        font-style: normal;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100%;
                        width: 100%;
                    }
                    .container {
                        padding: 0px;
                    }
                    h1 {
                        color: #f82efa;
                        transition: color 0.5s ease-in-out;
                        font-size: 100px;
                    }
                    h1:hover {
                        color: #fa4dfb;
                        animation: shake 0.5s ease-in-out;
                        cursor: pointer;
                    }
                    @keyframes shake {
                        0% { transform: translateX(0); }
                        25% { transform: translateX(-5px) rotate(-3deg); }
                        50% { transform: translateX(5px) rotate(3deg); }
                        75% { transform: translateX(-5px) rotate(-3deg); }
                        100% { transform: translateX(0) rotate(0); }
                    }
                </style>
                <link rel="icon" type="image/png" sizes="16x16" href="favicon.ico">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
            </head>
            <body>
                <div class="container">
                    <h1>Welcome to my site!</h1>
                </div>
            </body>
        </html>
    """

@app.get('/about', response_class=HTMLResponse)
def get_about():
    return """
            <html>
                <head>
                    <title>About me</title>
                    <style>
                        body {
                            background-color: #f3fbc7;
                            margin: 0;
                            padding: 0;
                            font-family: "Pacifico", cursive;
                            font-style: normal;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100%;
                            width: 100%;
                        }
                        .container {
                            padding: 0px;
                            text-align: center;
                        }
                        h1 {
                            color: #badb1e;
                            transition: color 0.5s ease-in-out;
                            font-size: 50px;
                        }
                        h1:hover {
                            color: #b7cc4d;
                            cursor: pointer;
                        }
                        p {
                            color: #57650d;
                        }
                    </style>
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
                </head>
                <body>
                    <div class="container">
                        <h1>About me</h1>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    </div>
                </body>
            </html>
        """

def run():
    store.get_categories()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
