import unittest

from test import templateEnv, json


class IOSTETestCase(unittest.TestCase):

    def test_ios_te(self):
        """

        :return:
        """
        TEMPLATE_FILE = "ios_te_tunnel.j2"
        template = templateEnv.get_template(TEMPLATE_FILE)

        with open("../json/R6_tunnels.json", "r") as json_file:
            data = json.load(json_file)
            self.assertIsInstance(data, dict)

        result = template.render(**data).replace("\r\n", "")
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
