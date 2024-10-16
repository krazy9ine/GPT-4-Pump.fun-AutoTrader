use anchor_lang::prelude::*;

declare_id!("YourProgramPublicKey");

#[program]
pub mod auto_trade {
    use super::*;
    pub fn execute_trade(ctx: Context<ExecuteTrade>, amount: u64) -> Result<()> {
        Ok(())
    }
}

#[derive(Accounts)]
pub struct ExecuteTrade<'info> {
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    pub system_program: Program<'info, System>,
}
