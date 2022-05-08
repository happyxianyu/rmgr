import logging
import asyncio

from rmgr import *

proj_root_path = Path(__file__).prnt.prnt
test_tmp_path = proj_root_path/Path('tmp/test')

async def atest_init():
    init_rmgr(test_tmp_path)
    import rmgr.core as rmgr
    logging.info(rmgr.path)

    

def test_init():
    asyncio.run(atest_init())
    return True