from flask import Flask, render_template, request
import ip_sum as ip_functions

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():

    addresses = []
    subnet = None

    if request.method == "POST":

        action = request.form.get("action")

        if action == "available":

            ip = request.form.get("ipaddr")
            subnet_mask = request.form.get("subnet")

            subnet_mask = int(subnet_mask.replace("/", ""))

            addresses = ip_functions.get_valid_ip(ip, subnet_mask)

        elif action == "summarize":

            ip_one = request.form.get("addrone")
            ip_two = request.form.get("addrtwo")

            subnet = ip_functions.get_summarized_subnet(
                ip_functions.ip_to_bits(ip_one),
                ip_functions.ip_to_bits(ip_two)
            )

    return render_template(
        "index.html",
        addresses=addresses,
        subnet=subnet
    )

if __name__ == "__main__":
    app.run(debug=True, port = 8080)