import asyncio

async def my_task(seconds):
    """
    A task to do for a number of seconds
    """
    print("my_task() - this task is taking {} seconds to complete".format(seconds))
    await asyncio.sleep(seconds)
    return 'my_task() - task finished'


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print('main() - task creation started')
        task_oj = loop.create_task(my_task(seconds=2))
        loop.run_until_complete(task_oj)
    finally:
        loop.close()

    print("main() - task result is {}".format(task_oj.result()))
