import asyncio
from rmgr import *

proj_root_path = Path(__file__).prnt.prnt
test_tmp_path = proj_root_path/Path('tmp/test')

async def atest_init():
    rctx = ResContext(test_tmp_path)

async def atest_run_shellscript_async():
    rctx = ResContext(test_tmp_path)
    path = rctx.path
    res = await rctx.run_shellscript_async(r'echo "Hello world!" > hello_world.txt', cwd=path.cache)
    assert((path.cache/'hello_world.txt').exists())
    

def test_proc():
    asyncio.run(atest_run_shellscript_async())
    return True

