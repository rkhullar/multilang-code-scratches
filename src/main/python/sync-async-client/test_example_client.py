from example_client import ExampleClient


def test_sync():
    print('test sync')
    client = ExampleClient(enable_async=False)
    result = client.read_pets_v2()
    print(result)


async def test_async():
    print('test async')
    client = ExampleClient(enable_async=True)
    result = await client.read_pets_v2()
    print(result)


async def main():
    test_sync()
    await test_async()


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
