import logging
import sys

import chardet

from rmgr import *
import asyncio

proj_root_path = Path(__file__).prnt.prnt
test_tmp_path = proj_root_path/Path('tmp/test')
init_rmgr(test_tmp_path)

from rmgr.core import *


async def atest_run_shellscript_async():
    res = await run_shellscript_async(r'echo "Hello world!" > hello_world.txt', cwd=path.cache)
    assert((path.cache/'hello_world.txt').exists())
    

def test_proc():
    asyncio.run(atest_run_shellscript_async())
    return True

