import copy
import importlib.util
import unittest
from pathlib import Path

class CatalogTests(unittest.TestCase):
    def checker(self):
        path=Path(__file__).resolve().parents[1]/'scripts/check_catalog.py'
        self.assertTrue(path.exists(), 'catalog validator does not exist')
        spec=importlib.util.spec_from_file_location('checker',path)
        m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
        return m

    def fixture(self):
        return {'schema_version':1,'captured_at':'2026-10-08T13:02:55+00:00',
                'repositories':[{'name':'tool','lifecycle':'product','upstream':None,'pull_requests':[]},
                {'name':'copy','lifecycle':'fork','upstream':'someone/tool','pull_requests':[]}]}

    def test_typed_catalog(self):
        self.assertEqual(self.checker().validate(self.fixture()), {'total':2,'forks':1})

    def test_duplicate_missing_parent_and_unsafe_name(self):
        m=self.checker()
        for kind in ('duplicate','no-parent','unsafe-name','bad-role','unexpected-parent'):
            d=self.fixture()
            if kind=='duplicate':d['repositories'].append(copy.deepcopy(d['repositories'][0]))
            elif kind=='no-parent':d['repositories'][1]['upstream']=None
            elif kind=='unsafe-name':d['repositories'][0]['name']='../bad'
            elif kind=='bad-role':d['repositories'][0]['lifecycle']='bogus'
            else:d['repositories'][0]['upstream']='someone/tool'
            with self.assertRaises(ValueError):m.validate(d)

    def test_pr_identity_and_status(self):
        m=self.checker()
        for pr in ({'number':1,'state':'merged','url':'https://github.com/wrong/repo/pull/1'},
                   {'number':True,'state':'open','url':'https://github.com/someone/tool/pull/1'},
                   {'number':1,'state':'bogus','url':'https://github.com/someone/tool/pull/1'}):
            d=self.fixture();d['repositories'][1]['pull_requests']=[pr]
            with self.assertRaises(ValueError):m.validate(d)

    def test_search_total_requires_explicit_exclusions(self):
        m=self.checker();d=self.fixture()
        d['pr_search']={'total_count':1,'counts':{'open':0,'closed':1,'merged':0}}
        with self.assertRaises(ValueError):m.validate(d)
        d['excluded_pull_requests']=[{'number':1,'state':'closed',
            'url':'https://github.com/263311487-ux/awesome-claude-code/pull/1',
            'reason':'Owned fork PR, not a parent repository PR'}]
        self.assertEqual(m.validate(d),{'total':2,'forks':1})
        d['pr_search']['counts']['closed']=2
        with self.assertRaises(ValueError):m.validate(d)

if __name__=='__main__':unittest.main()
