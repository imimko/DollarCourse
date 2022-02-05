from twirp.context import Context
from twirp.exceptions import TwirpServerException

import dollar_cource_twirp, dollar_cource_pb2

client = dollar_cource_twirp.DollarcourseClient("http://127.0.0.1:3000")

response = client.GetCourse(ctx=Context(), request=dollar_cource_pb2.Mes())
print(response)