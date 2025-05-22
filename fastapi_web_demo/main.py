from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello", response_class=HTMLResponse)
def hello_html():
    return """
    <html>
        <head>
            <title>Hello Page</title>
            <style>
                body {
                    background-color: #f0f4f8;
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    max-width: 600px;
                    margin: 50px auto;
                    background: #fff;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    padding: 32px;
                    text-align: center;
                }
                h1 {
                    color: #0077cc;
                }
                p {
                    color: #333;
                }
                img {
                    width: 200px;
                    margin: 16px 0;
                    border-radius: 8px;
                    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
                }
                .chatbox {
                    margin-top: 32px;
                    padding: 16px;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    background: #f9fafb;
                }
                .chatbox input[type="text"] {
                    width: 70%;
                    padding: 8px;
                    border-radius: 4px;
                    border: 1px solid #ccc;
                }
                .chatbox input[type="submit"] {
                    padding: 8px 16px;
                    border-radius: 4px;
                    border: none;
                    background: #0077cc;
                    color: #fff;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Ganesh Bot </h1>
                <!--img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" /-->
                <!--p>This is an HTML response with some CSS styling and an image.</p-->
                <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80" alt="Sample Unsplash" />
                <div class="chatbox">
                    <form action="/chatbot" method="post">
                        <input type="text" name="message" placeholder="Type your message..." required />
                        <input type="submit" value="Send" />
                    </form>
                </div>
            </div>
        </body>
    </html>
    """

@app.post("/chatbot", response_class=HTMLResponse)
async def chatbot(message: str = Form(...)):
    # Simple echo chatbot logic
    bot_reply = f"You said: {message}"
    return f"""
    <html>
        <head>
            <title>Chatbot Reply</title>
            <style>
                body {{
                    background-color: #f0f4f8;
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    max-width: 600px;
                    margin: 50px auto;
                    background: #fff;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    padding: 32px;
                    text-align: center;
                }}
                .chatbox {{
                    margin-top: 32px;
                    padding: 16px;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    background: #f9fafb;
                }}
                .chatbox input[type="text"] {{
                    width: 70%;
                    padding: 8px;
                    border-radius: 4px;
                    border: 1px solid #ccc;
                }}
                .chatbox input[type="submit"] {{
                    padding: 8px 16px;
                    border-radius: 4px;
                    border: none;
                    background: #0077cc;
                    color: #fff;
                    cursor: pointer;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Chatbot Reply</h1>
                <div class="chatbox">
                    <p><b>You:</b> {message}</p>
                    <p><b>Bot:</b> {bot_reply}</p>
                    <form action="/chatbot" method="post">
                        <input type="text" name="message" placeholder="Type your message..." required />
                        <input type="submit" value="Send" />
                    </form>
                    <p><a href="/hello">Back to Hello Page</a></p>
                </div>
            </div>
        </body>
    </html>
    """