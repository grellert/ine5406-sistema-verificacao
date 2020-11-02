library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_signed.all;

entity top is
    port(clk, rst: in std_logic;
         A, B: in std_logic_vector(3 downto 0);
         S: out std_logic_vector(4 downto 0));
end top;

architecture rtl of top is
signal regA, regB: std_logic_vector(3 downto 0);

begin

    process(clk, rst)
    begin
        if rst = '1' then
            regA <= (others => '0');
            regB <= (others => '0');
        elsif clk'event and clk = '1' then
            regA <= A;
            regB <= B;
        end if;
    end process;
    
    S <= (regA(3) & regA) + (regB(2) & regB);
end rtl;