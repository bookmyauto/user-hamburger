from response import Response
from sql import Sql

class Hamburger:
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    #                                                                   GETTING NAME                                                                                                    #
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    @staticmethod
    def get_name(user_number):
        conn    = None
        try:
            conn, cur   = Sql.get_connection()
            sql_query   = "select name from users where number = '{0}'"
            cur.execute(sql_query.format(user_number))
            data        = cur.fetchone()
            name        = data[0]
            conn.commit()

            conn.close()
            result      = Response.make_response(200, "", "", name = name)
            return result
        except Exception as e:
            if conn is not None:
                conn.close()
            logging.error("Error in setting name for user number " + str(user_number) + ": " + str(e))
            return Response.default_error

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    #                                                                   SETTING NAME                                                                                                    #
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    def set_name(user_number, name):
        conn    = None
        try:
            conn, cur   = Sql.get_connection()
            sql_query   = "update users set name = '{0}' where number = '{1}'"
            cur.execute(sql_query.format(name, user_number))
            conn.commit()

            conn.close()
            result      = Response.make_response(200, "name changed", "Your name has been changed")
            return result
        except Exception as e:
            if conn is not None:
                conn.close()
            logging.error("Error in setting name for user number " + str(user_number) + ": " + str(e))
            return Response.default_error
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    #                                                                   GET HISTORY                                                                                                     #
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    @staticmethod
    def history(user_number, count, last_timestamp):
        conn    = None
        try:
            conn, cur   = Sql.get_connection()
            sql_query   = "select * from user_history where timestamp < {0} limit count";
            cur.execute(sql_query)
            data        = cur.fetchall()

            output      = {}
            ind         = 0
            for r in data:
                _user_number                = str(r[0])
                _booking_id                 = str(r[1])
                timestamp                   = r[2]
                output[ind]                 = {}
                output[ind]["userNumber"]   = _user_number
                output[ind]["bookingId"]    = _booking_id
                output[ind]["timestamp"]    = timestamp
                ind                         = ind + 1

            conn.close()
            result      = Response.make_response(200,"","History fetched", history = output)
            return result
        except Exception as e:
            if conn is not None:
                conn.close()
            logging.error("Error in showing history for user number " + str(user_number) + ": " + str(e))
            return Response.default_error
