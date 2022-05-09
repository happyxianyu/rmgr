import asyncio

from rmgr import *

proj_root_path = Path(__file__).prnt.prnt
test_tmp_path = proj_root_path/Path('tmp/test')

async def atest_init():
    rctx = ResContext(test_tmp_path)
    

def test_init():
    asyncio.run(atest_init())
    return True

