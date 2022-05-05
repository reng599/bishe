# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List
from Tea.core import TeaCore

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Dysmsapi20170525Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'dysmsapi.aliyuncs.com'
        return Dysmsapi20170525Client(config)

    @staticmethod
    def main(
        phone:str,
        password:str
    ) -> None:
        template = '{"code":"%s"}' % password
        client = Sample.create_client('LTAI5tF9UDugY5KhYGkeV1o8', 'NiVg6up1tQRc7x4gMgjOTjgYvZMDbS')
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            sign_name='阿里云短信测试',
            template_code='SMS_154950909',
            phone_numbers=phone,
            template_param=template
        )
        resp = client.send_sms(send_sms_request)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))
        

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('ACCESS_KEY_ID', 'ACCESS_KEY_SECRET')
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            sign_name='阿里云短信测试',
            template_code='SMS_154950909',
            phone_numbers='18633309052',
            template_param='{"code":"1234"}'
        )
        resp = await client.send_sms_async(send_sms_request)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
