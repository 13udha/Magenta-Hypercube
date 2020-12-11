# Responses

An intent handler function can return three different types of objects. Any other returned object results in error.

## Response

*`skill_sdk.responses.Response`*

Any valid call of an intent handler may return `Response` type object. 
If a call of the intent is valid, the requested user action processed as intended. 
Furthermore, it covered any exception from the normal processing that is handled by notifying the client/user about the result. 
In other words: Everything that is not an unrecoverable error.

You can give all attributes of a `Response` instance to the `__init__` call or set them later.

A `Response` instance has the following attributes:

- **type_**: This is the type of the response. It can be either of `skill_sdk.responses.RESPONSE_TYPE_ASK`, `skill_sdk.responses.RESPONSE_TYPE_TELL` or `skill_sdk.responses.RESPONSE_TYPE_ASK_FREETEXT`.
- **text**: This is the string type text message that the client reads out to the user. It should be a question for `RESPONSE_TYPE_ASK`/`RESPONSE_TYPE_ASK_FREETEXT` and a statement for `RESPONSE_TYPE_TELL`. If the text is wrapped in a `<speak>` tag, it is interpreted as SSML.
- **card**: A card can be attached to the response. It hast to be an instance of `SimpleCard` or its subclasses. The card is presented in the companion app of the user.
- **result**: This is the result in a machine readable form. It can also be ``None``.

### Cards

Cards deliver additional information to the user via the companion app on the smartphone.
If a card is attached to the `Response`, it appears there.

## Re-prompts

A re-prompt response is a special type of `RESPONSE_TYPE_ASK` response. It is implemented as a measure to limit a number of re-prompts.

Suppose your skill receives a number that must be in a range between 1 and 10. 
If user answers with a number outside of a range, you want to issue a re-prompt notifying user about erroneous input. 
If user again answers with a number outside, you issue a re-prompt once again.
If user's input is again invalid, you might want to give up and stop re-prompting.  

`Reprompt` response sets a number of re-prompts as a session value, increasing it with every prompt to user.
When the number of re-prompts reaches maximum, a simple `RESPONSE_TYPE_TELL` is returned with a `stop_text` that is set when constructing `Reprompt` response.  

## ErrorResponse

*`skill_sdk.responses.ErrorResponse`*

An intent handler can return an `ErrorResponse` explicitly. If intent handler fails, the `ErrorResponse` is also returned.

The following combinations of an `ErrorResponse` are defined:

- **wrong intent**: `ErrorResponse(code=1, text="intent not found")` → *HTTP code: 404*
- **invalid token**: `ErrorResponse(code=2, text="invalid token")` → *HTTP code: 400*
- **locale,… missing**: `ErrorResponse(code=3, text="Bad request")` → *HTTP code: 400*
- **unhandled exception**: `ErrorResponse(code=999, text="internal error")` → *HTTP code: 500*

## String

If just a string is returned from the intent handler function, it is equivalent to returning `Response(text=the_returned_string)`.
As a result, the text is read out to user.
