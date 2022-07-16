#from bolsa import B3AsyncBackend
#
#
#b3_httpclient = B3AsyncBackend(
#    username='102.947.537-70',
#    password='4shatfQ3!',
#    captcha_service=None  # `captcha_service` não é obrigatório ainda
#)
#
#brokers = await b3_httpclient.get_brokers_with_accounts()
#assets_extract = (
#    await b3_httpclient.get_brokers_account_portfolio_assets_extract(
#        brokers=brokers
#    )
#)
#
#print(assets_extract) # Todos os seus ativos consolidados no CEI
#
#await b3_httpclient.session_close()
#await b3_httpclient.connection_close()




import asyncio
import logging

from bolsa import B3AsyncBackend

logging.basicConfig(
    format=(
        '%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] '
        '%(message)s'
    ),
    datefmt='%Y-%m-%d,%H:%M:%S',
    level=logging.DEBUG
)


async def main():
    from datetime import datetime
    start_datetime = datetime.now()
    logging.info(f'Starting... {start_datetime}')
    b3_httpclient = B3AsyncBackend(
        username='102.947.537-70',
        password='4shatfQ3!',
        captcha_service=None  # captcha_service is not required yet
    )
    brokers = await b3_httpclient.get_brokers_with_accounts()
    assets_extract = (
        await b3_httpclient.get_brokers_account_portfolio_assets_extract(
            brokers=brokers
        )
    )
    print(assets_extract)
    await b3_httpclient.session_close()
    await b3_httpclient.connection_close()

    logging.info(f'Finish script... {datetime.now() - start_datetime}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



