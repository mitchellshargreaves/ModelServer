from app import app
from flask import jsonify, request
from werkzeug.exceptions import HTTPException
from torch import FloatTensor

from evaluator import anomaly_evaluator

@app.route('/')
def home():
   return "hello world!"

# Populated from this page of exceptions:
# http://werkzeug.pocoo.org/docs/0.14/exceptions/
ERROR_TEXT_CODES = {
    400: "bad_request",
    401: "unauthorized",
    403: "forbidden",
    404: "not_found",
    405: "method_not_allowed",
    406: "not_acceptable",
    408: "request_timeout",
    409: "conflict",
    410: "gone",
    411: "length_required",
    412: "precondition_failed",
    413: "request_entity_too_large",
    414: "request_uri_too_large",
    415: "unsupported_media_type",
    416: "requested_range_not_satisfiable",
    417: "exceptation_failed",
    428: "precondition_required",
    429: "too_many_requests",
    431: "request_header_fields_too_large",
    500: "internal_error",
    501: "not_implemented",
    502: "bad_gateway",
    503: "service_unavailable"
}

# Handle exceptions
app.config['TRAP_HTTP_EXCEPTIONS'] = True

@app.errorhandler(Exception)
@app.errorhandler(500)
def unexpected_error_handler(error):
    """
    Prevent Flask from returning HTML errors for HTTP excceptions
    Args:
        error: The thrown http or internal error
    Returns:
        message: A description of what caused the error
        code: The text code
        status_code (int): The status code of the error

    """
    # Return the error information
    if isinstance(error, HTTPException):
        response = jsonify({
            "ok": False,
            "error": {
                "message": error.description,
                "code": ERROR_TEXT_CODES[error.code],
                "status_code": error.code
            }
        })
        response.status_code = error.code

    # Not a HTTP error (internal)
    else:
        response = jsonify({
            "ok": False,
            "error": {
                "message": "An unexpected internal error occurred",
                "code": "internal_error",
                "status_code": 500
            }
        })
        response.status_code = 500
    return response

@app.route('/anomaly', methods=['GET'])
def anomaly():
    """
    Runs the malaria detecting model on a supplied image
    Body:
      image (png): The image to be segmented
    Returns:
      filename: The image's filename
      prediction: Evaluator's predicton
    """
    # Read file details from the request
    series = request.form["series"]
    series = series[1:-1].replace(',', '')
    series = series.split()
    series = [float(x) for x in series]
    series = FloatTensor(series)
    print(series)

    # Run evaluator on series
    prediction = anomaly_evaluator(series)

    return jsonify({
        "ok": True,
        "prediction": prediction
    })