library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.std_logic_arith.all;
use work.p.all;
entity reg_interface is
	port(
		clk   : in  std_logic;
		rst   : in  std_logic;
		addr  : in  unsigned(32 downto 0);
		data  : in  std_logic_vector(32 downto 0);
		write : in  std_logic;
		foo   : out std_logic_vector(32 downto 0);
		bar   : out std_logic_vector(32 downto 0)
	);
end entity reg_interface;

architecture RTL of reg_interface is
begin
	name : process(clk, rst) is
	begin
		if rst = '1' then
			foo <= (others => 0);
			bar <= (others => 0);
		elsif rising_edge(clk) then
			if write = '1' then
				case to_integer(addr) is
					when foo_address =>
						foo <= data;
					when bar_address =>
						bar <= data;
					when others =>
						null;
				end case;
			end if;
		end if;
	end process name;
end architecture RTL;
